import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

lowerBorderLandmarkStruct = np.array([0, 10, 20])   # enter The HSV values for the black bottem part of the landmarks
upperBorderLandmarkStruct = np.array([25, 30, 255]) # enter The HSV values for the black bottem part of the landmarks

lowerBorderLandmarkTop = np.array([0, 10, 20])    # enter The HSV values for the Round Top part of the landmarks
upperBorderLandmarkTop  = np.array([25, 30, 255]) # enter The HSV values for the Round Top part of the landmarks



folderPath = input("pleas enter the folder path:")
def RemoveLandmarks(path):
    global lowerBorderLandmarkStruct
    global upperBorderLandmarkStruct
    global lowerBorderLandmarkTop
    global upperBorderLandmarkTop
    imageInput = cv2.imread(path)
    imageHSV = cv2.cvtColor(imageInput, cv2.COLOR_BGR2HSV)
    maskOne = cv2.inRange(imageHSV, lowerBorderLandmarkStruct, upperBorderLandmarkStruct)
    maskTwo = cv2.inRange(imageHSV, lowerBorderLandmarkTop, upperBorderLandmarkTop)
    image = cv2.inpaint(imageInput, maskOne, 50, cv2.INPAINT_NS)
    image = cv2.inpaint(image, maskTwo, 50, cv2.INPAINT_NS)
    cv2.imwrite(path, image)




onlyfiles = [join(folderPath, f) for f in listdir(folderPath) if isfile(join(folderPath, f))]
counter = 1
for file in onlyfiles:
    RemoveLandmarks(file)
    print(str(counter) + "/" +str(len(onlyfiles)))
    counter = counter + 1
