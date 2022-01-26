"""
@author: Osama Shakeel
             
            ---Hough Transform---
            
Hough Transform is a popular technique to detect any shape,
if you can represent that shape in mathematical form. 
It can detect the shape even if it is broken or distorted a 
little bit.
functions: cv2.HoughLines(), cv2.HoughLinesP()

We represent shapes with the help of lines.
And line are expressed for Hough Transform by --
Cartesian CS(cordinate system) --> y= mx+c and Polar CS --> xcos0+ysin0

"""
import cv2
import numpy as np

img = cv2.imread('D:\\music\\chess.jpg')
img = cv2.resize(img,(400,400))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,10,200,apertureSize = 3)

#function accept parameter(img,rho,theta)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
#rho value -- distance resolution of pixels
#thetha - angle resolution
#line threshold
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(255,0,255),2)

cv2.imshow("edge",edges)
cv2.imshow("lines",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
