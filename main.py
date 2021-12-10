import sys
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os
from functions import *
from mapping import *
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

        logAngleLegLeft = []
        logAngleLegRight = []

        logAngleArmLeft = []
        logAngleArmRight = []

        logAngleShoulderArmLeft = []
        logAngleShoulderArmRight = []

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

            logging.debug("Distance")
            logging.debug("Sholder : {:.2f} cm".format(shoulderDistance*100))
            logging.debug("")
            logging.debug("ArmLeft : {:.2f} cm".format(armDistanceLeft*100))
            logging.debug("ArmRight : {:.2f} cm".format(armDistanceRight*100))
            logging.debug("")
            logging.debug("#1 Check if arm angle are equivalent when walking")
            logging.debug("AngleArmLeft : {:.2f} degree".format(angleArmLeft))
            logging.debug("AngleArmRight : {:.2f} degree".format(angleArmRight))
            logAngleArmLeft.append(angleLegLeft)
            logAngleArmRight.append(angleLegRight)
            logging.debug("")
            logging.debug("#2 Check if arm neeb")
            logging.debug("AngleSholderArmLeft {:.2f} degree".format(angleSholderArmLeft))
            logging.debug("AngleSholderArmRight {:.2f} degree".format(angleSholderArmRight))
            logAngleShoulderArmLeft.append(angleSholderArmLeft)
            logAngleShoulderArmRight.append(angleSholderArmRight)
            logging.debug("")
            logging.debug("#3 Check if arm behind the back (Combine #2 #3)")
            logging.debug("")
            logging.debug("#4 Check if leg are fully stretch")
            logging.debug("AngleLegLeft : {:.2f} degree".format(angleLegLeft))
            logging.debug("AngleLegRight : {:.2f} degree".format(angleLegRight))
            logAngleLegLeft.append(angleLegLeft)
            logAngleLegRight.append(angleLegRight)
            logging.debug("")
            logging.debug("Hip : {:.2f} cm".format(hipDistance*100))
            logging.debug("LegLeft : {:.2f} cm".format(legDistanceLeft*100))
            logging.debug("LegRight : {:.2f} cm".format(legDistanceRight*100))
            logging.debug("Body : {:.2f} cm".format(bodyDistance*100))

        # Make directory prepare for output
        if not os.path.exists(outputFolder+person_folder+"/"+str(key)):
            os.makedirs(outputFolder+person_folder+"/"+str(key))

        logsAngle=[]
        logsAngle.append(logAngleLegLeft)
        logsAngle.append(logAngleLegRight)
        logsAngle.append(logAngleArmLeft)
        logsAngle.append(logAngleArmRight)
        logsAngle.append(logAngleShoulderArmLeft)
        logsAngle.append(logAngleShoulderArmRight)


        # Plot and save graph
        for logAngle,logAngleTitle in zip(logsAngle, logsAngleMapping):
            # Plot graph from log array
            plt.title(logAngleTitle)
            plt.plot(logAngle)
            # Save graph
            plt.savefig(outputFolder+person_folder+"/"+str(key)+"/"+logAngleTitle+".png")
            # Clear graph
            plt.clf()


