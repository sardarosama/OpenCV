"""
@author: Osama Shakeel
Image Read and Write 
"""

import cv2 

#load image in Colour mode
img1 = cv2.imread("D:\\music\\ava.jpg",1)
img1 = cv2.resize(img1,(760,600))

print("img 1 ", img1)
cv2.imshow("Colour image", img1)

#cv2.imread_GRAYSCALE: Load image in Grayscale mode
img2 = cv2.imread("D:\\music\\ava.jpg",0)
img2 = cv2.resize(img2,(760,600))

print("img 2", img2)
cv2.imshow("Gray image", img2)

#cv2.imread_UNCHANGED: Load image including ALpha Channel mode
img3 = cv2.imread("D:\\music\\ava.jpg",-1)
img3 = cv2.resize(img3,(760,600))

print("img 3", img3)
cv2.imshow("Unchanged Image", img3)


cv2.waitKey(0)
cv2.destroyAllWindows()