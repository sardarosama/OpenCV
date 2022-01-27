"""
@author: Osama Shakeel 

          ---Feature Detection and Description---
          
For understanding  this we recall jisaw puzzle game where we combine multiple 
small pieces in correct order by identifying its corners , shape and pattern.

On the basis of all these we all detect corners in images with so many approaches,

            ---Harris Corner Detection--- 

OpenCV has the function cv2.cornerHarris() for this purpose. 
Its arguments are : img - Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.
     
         
"""

import numpy as np
import cv2 as cv

img = cv.imread('D:\\music\\shapes.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)

#arguments are : grayscale Input image, it should float32 type, blockSize
res= cv.cornerHarris(gray, 2, 3, 0.04)

res = cv.dilate(res, None)

img[res > 0.01 * res.max()] = [0, 0, 255]  # marked color

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()