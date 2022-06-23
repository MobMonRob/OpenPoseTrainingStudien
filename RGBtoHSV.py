import cv2
import numpy as np

R = input("Red value:")
G = input("Green value:")
B = input("Blue value:")


Color = np.uint8([[[B,G,R ]]])
hsv_green = cv2.cvtColor(Color,cv2.COLOR_BGR2HSV)
print( "-----------")
print( "Hue:" + str(hsv_green[0][0][0]) )
print( "Saturation:" + str(hsv_green[0][0][1] ))
print( "value:" + str(hsv_green[0][0][2] ))