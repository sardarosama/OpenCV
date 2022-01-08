"""
@author: Osama Shakeel
Image Operations with Pixels ---

"""

import cv2
import numpy as np

#Read an Image ---
img = cv2.imread("D://music//ava.jpg")

img = cv2.resize(img, (600,400))
print("Shape == ", img.shape) # Return a tuple of numbers of rows, columns
print("No of Pixels ==", img.size) # Return Total numbers of pixels
print("Datatype ==", img.dtype) #Return image datatype
print("Image Type== ", type(img))

#Now try to split an image
#split -  return 3 channels of your image which is blue, green and red
#print(cv2.split(img))


b,g,r = cv2.split(img)
"""
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
"""
#Now if we want to merge images
mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb", mr1)

mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr", mr2)

mr3 = cv2.merge((r,b,g))
cv2.imshow("rbg",mr3)


cv2.imshow("res", img)
cv2.waitKey(0)
cv2.destroyAllWindows()