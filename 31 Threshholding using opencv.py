"""

@author: Osama Shakeel
Threshholding using opencv
Thresholding is of three types. Simple, Adoptive and Sue thresholding
Simple Thresholding accept four paramters(img, pixel_thresh, max_thresh_pixel, style)

"""
import cv2
import numpy as np

img =cv2.imread("D://music//black_white.png", 0)
img = cv2.resize(img, (300,300))
cv2.imshow("orignal", img)

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


cv2.imshow("Binary threshold ==", th1)
cv2.imshow("Binary inverse thresh ==", th2)
cv2.imshow("Trunc thresh ==", th3)
cv2.imshow("Tozero thresh ==", th4)
cv2.imshow("Tozero Inverse thresh ==", th4)

cv2.waitKey(0)
cv2.destroyAllWindows()
