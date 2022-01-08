"""
@author: Osama Shakeel
Detect Color in an Image (Masking)
HSV -  Hue saturation value
Hsv is use to separate image information on the basis of color luminous or intensity.
We use Hsv where we perform operation on the basis of color.
HSV related to hexaon color model
H - hue - use to select color from 360 portion 
staturation is amount of color  which is selected in hue.(color shades)
V  -  value which is brightness of the color.

"""

import cv2
import numpy as np

frame = cv2.imread('D://music//color_balls.jpg')
while True:
    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
   
    l_v = np.array([110,50,50])
    u_v = np.array([130,235,225])
    
    #Creating Mask
    mask = cv2.inRange(hsv, l_v, u_v)
    #filter mask with image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()