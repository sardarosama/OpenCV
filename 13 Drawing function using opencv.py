"""
@author: Osama Shakeel
Drawing Function in opencv

"""

import numpy as np
import cv2

img = cv2.imread("D://music//ava.jpg")
#For resizing

img = cv2.resize(img, (500,600))

#Here to draw a line we need to pass five parameters
#(img, starting, ending, color, thickness)

img = cv2.line(img,(0,0), (200,200), (255, 133,243), 4) #Color Format BGR

#To create an arrrowed line we will pass five parameters
#(img, starting, ending, color, thickness)
img = cv2.arrowedLine(img, (0,0),(244,333),(233,125,13),6)

#To create a rectangle the parameters are
#(img,start_co, end_co,thickness)
img = cv2.rectangle(img, (233,10), (510,128), (126,24,10),6)

#To create circle paramters are
#(img,start_co,radius, color, thickness)
img = cv2.circle(img, (255,300), 49,  (123,233,233),4) 

#To write and using Font parameters are
#(img, text, start_co, font, fontsize,color, thickness, linetype)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,"AVA", (20,500),font, 4, (0,125,255), cv2.LINE_AA)

#Ellipse accept paramters (img, start_co, (length, heigth) color, thickness,)
img = cv2.ellipse(img,(200,300), (100,50), 0,0,360,155,5)  #0,0 are rotating point

cv2.imshow("Res", img)
cv2.waitKey(0)
cv2.destroyAllWindows()