"""
@author: Osama Shakeel
Extracting Object from an Image and place on another image
Random Figure ROI or Background Subtraction
"""
import cv2
import numpy as np

# Load two images
img1 = cv2.imread("D://music//hero1.jpg")
img2 = cv2.imread("D://music//strom_breaker.jpg")


img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

#I want to fix img2 data into img1
r,c,ch = img2.shape
print(r,c,ch)

roi = img1[0:r,0:c]

#Now creating mask for img1
img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Create Mask using Threshold
_, mask = cv2.threshold(img_gray, 50,255, cv2.THRESH_BINARY)

#remove bg
mask_inv = cv2.bitwise_not(mask)

#put mask into roi
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

#Take only region of figure from orignal image.
img2_fg = cv2.bitwise_and(img2, img2, mask= mask)

#put img in roi and modify main image
res = cv2.add(img1_bg, img2_fg)

final = img1
final[0:r, 0:c] = res


cv2.imshow("Thor",img1)
cv2.imshow("Strom breaker",img2)
cv2.imshow("roi ", roi)
cv2.imshow("gray==", img_gray)
cv2.imshow("mask ==", mask)
cv2.imshow("mask_inv==", mask_inv)
cv2.imshow("img1_bg==", img1_bg)
cv2.imshow("img2_fg==", img2_fg)
cv2.imshow("res==", res)
cv2.imshow("final", final)

cv2.waitKey(0)
cv2.destroyAllWindows() 