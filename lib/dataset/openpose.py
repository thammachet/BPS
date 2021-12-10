import os
import sys

# Configuration
basePath = '/mnt/HPE/Coding/AutoVideoProcess/'
targetVideoPath = basePath+sys.argv[1]+'/'
outputVideoPath = basePath+sys.argv[2]+'/'

os.chdir("/home/lab/openpose")
cwd = os.getcwd()
print("Current working directory is:", cwd)

# End Configuration
if(not os.path.isdir(outputVideoPath)):
    os.makedirs(outputVideoPath)

# Starting openpose
videos = os.listdir(targetVideoPath)
for video in videos:
    os.system('./build/examples/openpose/openpose.bin --video \''+targetVideoPath+video+'\' --write_video \''+outputVideoPath+video+'\' --write_json '+outputVideoPath+video+'json/')
# End openpose
