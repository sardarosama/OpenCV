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

"""
using loop to generate pyramid
load image into gray scale
"""
img = cv2.imread("D:\\music\\sam.jpeg")
img = cv2.resize(img,(700,700))

img1 = img.copy()
data = [img1]

for i in range(4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("res"+str(i),img1)

cv2.imshow("original==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()    
