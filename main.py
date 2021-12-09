import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import joblib
import matplotlib.pyplot as plt
import os
from functions import *


# Set the path to the folder with the data
os.getcwd()
os.chdir('/mnt/HPE/Coding/BodyRatio')
os.getcwd()

output = joblib.load('28.pkl')
print(output.keys())  

height = 2000
width = 2000
key = 4

logAngleLegLeft = []
logAngleLegRight = []

logAngleArmLeft = []
logAngleArmRight = []

logAngleShoulderArmLeft = []
logAngleShoulderArmRight = []

print(len(output[key]['joints3d']))
for frameIndex in range(len(output[key]['joints3d'])):
    joints =  output[key]['joints3d'][frameIndex]

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

    print("Distance")
    print("Sholder : {:.2f} cm".format(shoulderDistance*100))
    print()
    print("ArmLeft : {:.2f} cm".format(armDistanceLeft*100))
    print("ArmRight : {:.2f} cm".format(armDistanceRight*100))
    print()
    print("#1 Check if arm angle are equivalent when walking")
    print("AngleArmLeft : {:.2f} degree".format(angleArmLeft))
    print("AngleArmRight : {:.2f} degree".format(angleArmRight))
    logAngleArmLeft.append(angleLegLeft)
    logAngleArmRight.append(angleLegRight)
    print()
    print("#2 Check if arm neeb")
    print("AngleSholderArmLeft {:.2f} degree".format(angleSholderArmLeft))
    print("AngleSholderArmRight {:.2f} degree".format(angleSholderArmRight))
    logAngleShoulderArmLeft.append(angleSholderArmLeft)
    logAngleShoulderArmRight.append(angleSholderArmRight)
    print()
    print("#3 Check if arm behind the back (Combine #2 #3)")
    print()
    print("#4 Check if leg are fully stretch")
    print("AngleLegLeft : {:.2f} degree".format(angleLegLeft))
    print("AngleLegRight : {:.2f} degree".format(angleLegRight))
    logAngleLegLeft.append(angleLegLeft)
    logAngleLegRight.append(angleLegRight)
    print()
    print("Hip : {:.2f} cm".format(hipDistance*100))
    print("LegLeft : {:.2f} cm".format(legDistanceLeft*100))
    print("LegRight : {:.2f} cm".format(legDistanceRight*100))
    print("Body : {:.2f} cm".format(bodyDistance*100))



# %%
# Plot graph from log array
plt.title("Angle Leg Left")
plt.plot(logAngleLegLeft)
plt.show()

plt.title("Angle Leg Right")
plt.plot(logAngleLegRight,label='Right')
plt.show()

plt.title("Angle Arm Left")
plt.plot(logAngleArmLeft,label='Left')
plt.show()

plt.title("Angle Arm Right")
plt.plot(logAngleArmRight,label='Right')
plt.show()

plt.title("Angle Shoulder Arm Left")
plt.plot(logAngleShoulderArmLeft,label='Left')
plt.show()

plt.title("Angle Shoulder Arm Right")
plt.plot(logAngleShoulderArmRight,label='Right')
plt.show()



# %%



