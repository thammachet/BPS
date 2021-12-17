import sys
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os
from functions import *
import logging

# Configuration
inputFolder = "./vibe-input/"
outputFolder = "./output/"

logging.basicConfig(filename="log.txt", level=logging.DEBUG)


# List all folder in folder
vibe_folder= os.listdir("./vibe-input/")

for person_folder in vibe_folder:
    # Get file only end with ".pkl"
    pkl = [f for f in os.listdir("./vibe-input/"+person_folder) if f.endswith(".pkl")]
    # Pkl must be only one file
    if len(pkl) != 1:
        logging.info("PKL Model must be only one")
    # Load model
    model = joblib.load("./vibe-input/"+person_folder+"/"+pkl[0])

    for key in list(model.keys()):
        logging.debug("Processing "+str(key))
        height = 2000
        width = 2000

        logsAngle={
            "AngleLegLeft":[],
            "AngleLegRight":[],
            "AngleArmLeft":[],
            "AngleArmRight" :[],
            "AngleShoulderArmLeft" :[],
            "AngleShoulderArmRight" :[]
        }

        logging.debug(len(model[key]['joints3d']))
        for frameIndex in range(len(model[key]['joints3d'])):
            joints =  model[key]['joints3d'][frameIndex]

            shoulderDistance = distance(joints[2],joints[5])
            angleSholderArmLeft = angle_3(joints[5],joints[2],joints[3]) -90
            angleSholderArmRight = angle_3(joints[2],joints[5],joints[6]) -90

            armDistanceLeft = distance(joints[2],joints[3])+distance(joints[3],joints[4])
            angleArmLeft = angle_3(joints[2],joints[3],joints[4])

            armDistanceRight = distance(joints[5],joints[6])+distance(joints[6],joints[7])
            angleArmRight = angle_3(joints[5],joints[6],joints[7])

            hipDistance = distance(joints[27],joints[28])

            legDistanceLeft = distance(joints[9],joints[10])+distance(joints[10],joints[11])
            angleLegLeft = angle_3(joints[9],joints[10],joints[11])

            legDistanceRight = distance(joints[12],joints[13])+distance(joints[13],joints[14])
            angleLegRight = angle_3(joints[12],joints[13],joints[14])

            bodyDistance = distance(joints[39],joints[40])+distance(joints[40],joints[41])

            # Log
            logsAngle["AngleArmLeft"].append(angleLegLeft)
            logsAngle["AngleArmRight"].append(angleLegRight)
            
            logsAngle["AngleShoulderArmLeft"].append(angleSholderArmLeft)
            logsAngle["AngleShoulderArmRight"].append(angleSholderArmRight)
           
            logsAngle["AngleLegLeft"].append(angleLegLeft)
            logsAngle["AngleLegRight"].append(angleLegRight)

        # Make directory prepare for output
        if not os.path.exists(outputFolder+person_folder+"/"+str(key)):
            os.makedirs(outputFolder+person_folder+"/"+str(key))


        # Plot and save graph
        for logAngleTitle in logsAngle.keys():
            logAngle = logsAngle[logAngleTitle]
            # Plot graph from log array
            plt.title(logAngleTitle)
            plt.plot(logAngle)
            # Save graph
            plt.savefig(outputFolder+person_folder+"/"+str(key)+"/"+logAngleTitle+".png")
            # Clear graph
            plt.clf()


