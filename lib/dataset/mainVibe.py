import os
from subprocess import Popen
# Configuration
inputVideoPath = "InputVideo"
outputVideoPath = "OutputVideo"

# End Configuration


videos = os.listdir(inputVideoPath)
## Vibe
for idx,video in enumerate(videos):
   if (idx%2==0 and idx!=0):
       p.wait()
   p=Popen(['python3','vibe.py',outputVideoPath+"/"+video+'/FaceRecognition'+'/OutVideo',outputVideoPath+"/"+video+'/OutVibe'])
p.wait()

# Openpose
for idx,video in enumerate(videos):
    if (idx%2==0 and idx!=0):
        p.wait()
    p=Popen(['python','openpose.py',outputVideoPath+"/"+video+'/FaceRecognition'+'/OutVideo',outputVideoPath+"/"+video+'/OutOpenpose'])
p.wait()
