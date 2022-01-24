"""
@author: Osama Shakeel

        ----Canny Edge Detection using trackbars-----
        
Canny Edge Detection is a popular edge detection approach.
It is use  multi-stage algorithm to detect a edges.
It was developed by John F. Canny in 1986.


This approach combine with 5 steps.
 1) -  NOise reduction(gauss)),
 2) -Gradient calculation( ,
 3) - Non-maximum suppresson,
 4) - Double Threshold,
 5) - Edge Tracking by Hysteresis 

"""

import cv2
import numpy as np

#building trackbar with canny edge

#load image into gray scale
img = cv2.imread("D:\\music\\sam.jpeg")
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)

while True:
    a= cv2.getTrackbarPos('Threshold','Canny')
    
    print(a)
    res = cv2.Canny(img_gray,a,255)
    cv2.imshow("Canny",res)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()






























