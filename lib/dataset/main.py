import os
from subprocess import Popen

# Configuration
inputVideoPath = "InputVideo"
outputVideoPath = "OutputVideo"

# End Configuration


videos = os.listdir(inputVideoPath)

# Face Recognition
for idx,video in enumerate(videos):
    if (idx%2==0 and idx!=0):
        p.wait()
    p=Popen(['python','Video_face_recognition.py',inputVideoPath+'/'+video,outputVideoPath+"/"+video+'/FaceRecognition'+'/OutImage','Temp/'+video])
p.wait()

# Image to Video
for idx,video in enumerate(videos):
    if (idx%2==0 and idx!=0):
        p.wait()
    p=Popen(['python','imageToVideo.py',outputVideoPath+"/"+video+'/FaceRecognition'+'/OutImage',outputVideoPath+"/"+video+'/FaceRecognition'+'/OutVideo'])
p.wait()


    # os.system('python3 Video_face_recognition.py {} {}'.format(inputVideoPath+'/'+video,outputVideoPath+"/"+video))
# End openpose
