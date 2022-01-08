"""
@author: Osama Shakeel
Region of Interest (ROI) ---

"""
import cv2
import numpy as np

#read
img = cv2.imread("D://music//roi_opr.jpg")
img = cv2.resize(img,(800,800)) #Width, Height

#ROI (Region of Interest)
# (320,50) (440,205)
# [(y1:y2),(x1:x2)]

roi = img[50:205,320:440]

#Now passing data into it
img[50:205,431:551] = roi
img[50:205,531:651] = roi
img[50:205,200:320] = roi
img[50:205, 80:200] = roi

#Changing in y
img[200:355,320:440] = roi
img[350:505,320:440] = roi
cv2.imshow("res", img)


#cv2.imshow("res", roi)
#cv2.imshow("res", img)

cv2.waitKey(0)
cv2.destroyAllWindows()