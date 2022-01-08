"""
@author: Osama Shakeel
Image blending using opencv---
Here We use two important functions cv2.add(), cv2.addWeighted() etc.
Blending means addition of two images
if you want to blend two images then both have same size

"""
import cv2
import numpy as np

img1 = cv2.imread("D://music//roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread("D://music//bro_thor.jpg")
img2 = cv2.resize(img2,(500,700))
cv2.imshow("thor", img1)
cv2.imshow("bro-thor", img2)


#Now perform blending
#result = img1+img2  #numpy addition in this we get module between value
#cv2.imshow("res", result)

#result1 = cv2.add(img1,img2) #its your saturated oprn which means value to value
#cv2.imshow("res", result1)

#sum of both the weight  = w1+w2 = 1(max)
#function cv2.addWeighted(img1,wt1,img2,wt2,gama_val)
result2 = cv2.addWeighted(img1,0.8,img2,0.2,0)

cv2.imshow("res", result2)

cv2.waitKey(0)
cv2.destroyAllWindows()
