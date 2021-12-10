import cv2

# read video
cap = cv2.VideoCapture('Y:/HumanCut2.mp4')

folderIndex = 0
frameIndex = 0
prevBlack=False

# per frame
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect completely black frame
    if frame.all() == 0:
        if(not prevBlack):
            folderIndex += 1
            frameIndex = 0
            prevBlack = True
            print('Folder index: ' + str(folderIndex))
    else:
        prevBlack = False
        frameIndex += 1
    # save frame
    cv2.imwrite('Y:/HumanCut/' + str(folderIndex) + '/' + str(frameIndex) + '.jpg', frame)
