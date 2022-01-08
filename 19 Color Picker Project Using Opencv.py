
"""
Osama Shakeel
Color Picker Project Using OPencv

"""

import cv2
import numpy as np

def cross(x):
    pass

#Blank image 
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("Color Picker")

#Create Trackbar 
s1 = "0:OFF \n 1:ON"
cv2.createTrackbar(s1, "Color Picker", 0,1, cross)


#Creating trackbar for adjusting color
cv2.createTrackbar("R", "Color Picker", 0,255,cross)
cv2.createTrackbar("G", "Color Picker", 0,255,cross)
cv2.createTrackbar("B", "Color Picker", 0,255,cross)

while True:
    cv2.imshow("Color Picker", img)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
    
    #Now to get trackbar positions
    s = cv2.getTrackbarPos(s1, "Color Picker")
    r = cv2.getTrackbarPos("R", "Color Picker")
    g = cv2.getTrackbarPos("G", "Color Picker")
    b = cv2.getTrackbarPos("B", "Color Picker")
    
    if s == 0:
        img[:]= 0
    else:
        img[:]= [r,g,b]
        
cv2.destroyAllWindows()


