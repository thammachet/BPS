import os
import re
import cv2
import sys

# Configuration
# Common
outputFolderName =  sys.argv[2]

inputRootDir = sys.argv[1]

print("Output folder name: " + outputFolderName)
print("Input root dir: " + inputRootDir)

# Nesscesary function
def regex_text_before_jpg(text):
    regex = r'(.*)(\.jpg)'
    matches = re.search(regex, text)
    return matches

if(not os.path.isdir(outputFolderName)):
    os.makedirs(outputFolderName)

for folderPerson in os.listdir(inputRootDir):
    print("Processing Folder : "+str(folderPerson)+" ...")
    listOfImages = os.listdir(inputRootDir+"/"+folderPerson)
    # Sorting image from less index
    listOfImagesInt = []
    for imagesName in listOfImages:
        regexResult = regex_text_before_jpg(imagesName)
        if regexResult != None:
            listOfImagesInt.append(int(regexResult.group(1)))
    listOfImagesInt = sorted(listOfImagesInt, reverse=False)
    # End Sorting image

    # Change image to video
    if len(listOfImagesInt) != 0:
        img = cv2.imread(inputRootDir+"/"+str(folderPerson)+'/'+str(listOfImagesInt[0])+'.jpg')
        height, width, layers = img.shape
        size = (width,height)
        out = cv2.VideoWriter(outputFolderName+"/"+str(folderPerson)+".avi",cv2.VideoWriter_fourcc(*'DIVX'),29.97,size)
        for imagesName in listOfImagesInt:
            img = cv2.imread(inputRootDir+"/"+str(folderPerson)+'/'+str(imagesName)+'.jpg')
            out.write(img)
        out.release()
    # End Change image to video
