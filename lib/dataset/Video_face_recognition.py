import sys

# Standard PySceneDetect imports:
from scenedetect import VideoManager
from scenedetect import SceneManager

# For content-aware scene detection:
from scenedetect.detectors import ContentDetector

import cv2
import numpy as np
import os
import face_recognition
import shutil

import logging
import argparse

# Parser argument
parser = argparse.ArgumentParser(description='Auto video face recognition process')
parser.add_argument('target_video', type=str, help='Path to video file to process')
parser.add_argument('out_dir', type=str, help='Path to output directory')
parser.add_argument('--temp_folder',nargs='?', type=str, help='Path to temp folder')
parser.add_argument('--ratio',nargs='?', type=float, help='Ratio of valid frame')
parser.add_argument('--personMax',nargs='?', type=int, help='Max number of person')

args = parser.parse_args()

# Configuration
logging.basicConfig(filename="runing.log",level=logging.DEBUG,format='%(levelname)s - %(message)s')
# Common
targetVideo = args.target_video
outPutFolderName = args.out_dir
tempFolderName = args.temp_folder if args.temp_folder != None else "./temp"
Debug = False

# SceneDetection
enableSceneDetection = True
threshold = 30.0

# SceneSelection
frameRatio = float(args.ratio) if args.ratio != None else 0.6
personMax = float(args.personMax) if args.personMax != None else 1

# FaceDetection
method = 2
faceSimilarThreshold = 0

# End of configuration

logging.info("Processing video : %s" % targetVideo)
logging.info("Frame ratio : {} Person Max : {}".format(frameRatio,personMax))
video_path = targetVideo
cap = cv2.VideoCapture(targetVideo, 0)

# Scene detector
if(enableSceneDetection):
    # Create our video & scene managers, then add the detector.
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))

    # Improve processing speed by downscaling before processing.
    video_manager.set_downscale_factor()

    # Start the video manager and perform the scene detection.
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)

    scenes = scene_manager.get_scene_list()
    sceneCutPos = []
    for scene in scenes:
        sceneCutPos.append(scene[0].get_frames())

    logging.debug(sceneCutPos)

# End of scene detector

frame_index = 0
scene_count = 0
output_frame_index = 0
currentSceneCutPos = 0
previouseSceneCutPos = 0
faceDetectFrame = 0

# Check and create folder for result
if(not os.path.isdir(outPutFolderName)):
    os.makedirs(outPutFolderName)
if(not os.path.isdir(tempFolderName)):
    os.makedirs(tempFolderName)


# Varuable to save founded face
known_face_encodings=[]
known_face_names = []

def RegisterNewFace(face_encoding):
    known_face_encodings.append(face_encoding)
    known_face_index = known_face_names[-1]+1 if len(known_face_names) != 0 else 0
    known_face_names.append(known_face_index)
    faceNamesCount.append(0)
    # Create new folder for new face
    os.mkdir(outPutFolderName+'/'+str(known_face_index))
    return known_face_index

faceNamesCount = []

while True:
    # Reset neccesary variable
    face_names=[]
    ret, frame = cap.read()

    # Scene detect manager
    if(enableSceneDetection):
        try:
            if frame_index >= sceneCutPos[scene_count+1] or not ret :
                # New scene begin
                scene_count += 1
                currentSceneCutPos = sceneCutPos[scene_count]
                logging.info("Summary scene between "+str(previouseSceneCutPos)+" to "+str(currentSceneCutPos))
                logging.info("Number of face detect between scene : "+str(faceDetectFrame))
                logging.info("number of frame between scene : "+str(currentSceneCutPos-previouseSceneCutPos))
                # If face time during scene less than 85 percent
                if (faceDetectFrame/(currentSceneCutPos-previouseSceneCutPos)<frameRatio):
                    logging.infol("Not using this scene")
                    logging.info("Removing temp file")
                    for file in os.listdir(tempFolderName):
                        os.remove(os.path.join(tempFolderName,file))
                    output_frame_index -= currentSceneCutPos - previouseSceneCutPos

                maxFace = max(faceNamesCount)
                maxFaceIndex = faceNamesCount.index(maxFace)
                logging.info("Moving picture from temp to face folder "+str(maxFaceIndex))
                files = os.listdir(tempFolderName)
                for f in files:
                    shutil.move(os.path.join(tempFolderName,f),outPutFolderName+'/'+str(maxFaceIndex))

                faceDetectFrame = 0
                logging.info("Next scene")
                previouseSceneCutPos = currentSceneCutPos
                faceNamesCount = [0] * len(faceNamesCount)

        except:
            pass

    # End of Scene detect manager

    # If video is ended exist loop
    if not ret:
        break

    # Face recognition
    rgb_frame = frame[:,:,::-1]
    face_locations = face_recognition.face_locations(rgb_frame,model="cnn")
    face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        # Selecting method
        if method == 1:
            if True in matches:
                first_match_index=matches.index(True)
                name=known_face_names[first_match_index]
            else:
                name = RegisterNewFace(face_encoding)
        if method == 2:
            face_distances = face_recognition.face_distance(known_face_encodings,face_encoding)
            if len(face_distances) != 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index] and face_distances[best_match_index]>faceSimilarThreshold:
                    name=known_face_names[best_match_index]
                else:
                    name = RegisterNewFace(face_encoding)
            else:
                name = RegisterNewFace(face_encoding)

        face_names.append(name)
        faceNamesCount[int(name)] +=1
    numOfFace = 0
    for (top,right,bottom,left),name in zip(face_locations,face_names):
        if Debug:
            cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),4)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, str(name), (left, bottom + 50), font, 1.0, (255, 255, 255), 1)
        numOfFace+=1
    # End of face recognition

    # Scene manager
    if(numOfFace>0 and numOfFace<personMax+1):
        faceDetectFrame+=1

    # cv2.imshow('Video', frame)
    # if cv2.waitKey(1) == ord('a'):
    #     break

    cv2.imwrite(tempFolderName+"/"+str(output_frame_index)+'.jpg', frame)

    # Ending part of logic
    frame_index += 1
    output_frame_index +=1

for file in os.listdir(tempFolderName):
    os.remove(os.path.join(tempFolderName,file))
