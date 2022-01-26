"""
@author: Osama Shakeel 

              ---Hough Transform---
              
        Second Type of Hough Transformation
              
Hough Transform is a popular technique to detect any shape,
if you can represent that shape in mathematical form. 
It can detect the shape even if it is broken or distorted a 
little bit.
functions: cv2.HoughLines(), cv2.HoughLinesP()

#We represent shapes with the help of lines.
#And line are expressed for Hough Transform by --
#Cartesian CS(cordinate system) --> y= mx+c and Polar CS --> xcos0+ysin0

"""

import cv2
import numpy as np


img = cv2.imread('D:\\music\\chess.jpg')
img = cv2.resize(img,(400,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,20,250)

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=8,
                        maxLineGap=100)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(100,200,125),2)

cv2.imshow('lines', img)
cv2.imshow('edges', edges)

k = cv2.waitKey(0)
cv2.destroyAllWindows()























