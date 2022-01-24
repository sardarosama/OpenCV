"""
@author: Osama Shakeel

             ---Image Pyramids in OpenCV---

We use Image Pyramid because somethimes we work on same imge
but different resolution.e.g. searching face, eye in an image
and it vary image to image so in this case we create a set 
of images with diff. resolution which is called pyramid.
We also use these pyramids to blends the images.


There are two types of Image Pyramid-
 1) Gaussian Pyramid 
 2) Laplacian Pyramids

"""



import cv2
import numpy as np


#load image into gray scale
img = cv2.imread("D:\\music\\sam.jpeg")
img = cv2.resize(img,(700,700))

#Gaussian Pyramid Have 2 function-1) cv2.pyrUp(),2)-cv2.pyrDown()
#pyrdown----
pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)

#pyrup
#if we pyrup any pyrdown image both are not equal
pu1 = cv2.pyrUp(pd2)


#results------------------
cv2.imshow("original==",img)
cv2.imshow("pd1==",pd1)
cv2.imshow("pd2==",pd2)
cv2.imshow("pu1==",pu1)

cv2.waitKey(0)
cv2.destroyAllWindows()










