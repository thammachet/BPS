import cv2
import os

# read video
cap = cv2.VideoCapture('Y:/HumanCut2.mp4')

folderIndex = 0
frameIndex = 0
prevBlack=False

# check if video folder exists
if not os.path.exists('C:/HumanCut/'):
    os.makedirs('C:/HumanCut/')

# per frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect completely black frame
    if cv2.countNonZero(gray) == 0:
        if(not prevBlack):
            folderIndex += 1
            frameIndex = 0
            prevBlack = True
            print('Folder index: ' + str(folderIndex))
        print("Black frame")
    else:
        prevBlack = False
        frameIndex += 1
        print(frameIndex)

        # Check if folder exists
        if not os.path.exists('C:/HumanCut/' + str(folderIndex)):
            os.makedirs('C:/HumanCut/' + str(folderIndex))
        
        # save frame
        cv2.imwrite('C:/HumanCut/' + str(folderIndex) + '/' + str(frameIndex) + '.jpg', frame)
