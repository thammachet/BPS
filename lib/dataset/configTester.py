import os
from subprocess import Popen

# Configuration
inputVideoPath = '/mnt/HPE/Coding/AutoVideoProcess/InputVideo/Miss Universe 2018  Swimsuit Competition_1080p.mp4'
outputVideoPath = "./output_video/result"

# End Configuration


r = 0.0

# Face Recognition
# while r < 1:
#     r+=0.1
#     p1=Popen(['python','Video_face_recognition.py',inputVideoPath,outputVideoPath+'-'+str(round(r,2))+'-'+str(1)+'/image','--ratio',str(r),'--personMax',str(1),'--temp_folder','./temp1'])
#     p2=Popen(['python','Video_face_recognition.py',inputVideoPath,outputVideoPath+'-'+str(round(r,2))+'-'+str(2)+'/image','--ratio',str(r),'--personMax',str(2),'--temp_folder','./temp2'])
#     p3=Popen(['python','Video_face_recognition.py',inputVideoPath,outputVideoPath+'-'+str(round(r,2))+'-'+str(3)+'/image','--ratio',str(r),'--personMax',str(3),'--temp_folder','./temp3'])
#     p1.wait()
#     p2.wait()
#     p3.wait()

# Image to video
r = 0.0
while r < 1:
    r+=0.1
    p1=Popen(['python','imageToVideo.py',outputVideoPath+'-'+str(round(r,2))+'-'+str(1)+'/image',outputVideoPath+'-'+str(round(r,2))+'-'+str(1)+'/Outvideo'])
    p2=Popen(['python','imageToVideo.py',outputVideoPath+'-'+str(round(r,2))+'-'+str(2)+'/image',outputVideoPath+'-'+str(round(r,2))+'-'+str(2)+'/Outvideo'])
    p3=Popen(['python','imageToVideo.py',outputVideoPath+'-'+str(round(r,2))+'-'+str(3)+'/image',outputVideoPath+'-'+str(round(r,2))+'-'+str(3)+'/Outvideo'])
    p1.wait()
    p2.wait()
    p3.wait()
