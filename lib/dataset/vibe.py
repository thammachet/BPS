import os
import sys

# Configuration
codePath = '/mnt/HPE/VIBE/'
basePath = '/mnt/HPE/Coding/AutoVideoProcess/'
targetVideoPath = basePath+sys.argv[1]+'/'
outputVideoPath = basePath+sys.argv[2]+'/'

os.chdir("/mnt/HPE/VIBE")
cwd = os.getcwd()
print("Current working directory is:", cwd)

# End Configuration
if(not os.path.isdir(outputVideoPath)):
    os.makedirs(outputVideoPath)

# Starting openpose
videos = os.listdir(targetVideoPath)
for video in videos:
    print('python3 '+codePath+'demo.py --vid_file \''+targetVideoPath+video+'\' --output_folder \''+outputVideoPath+video+'/\' --save_obj')
    os.system('python3 '+codePath+'demo.py --vid_file \''+targetVideoPath+video+'\' --output_folder \''+outputVideoPath+'/\' --save_obj')
# End openpose
