"""
@author: Osama Shakeel
Example with all morphological operations

"""

import cv2
import numpy as np

img = cv2.imread('D:\\music\\girl.jpg',0)
img = cv2.resize(img,(300,300))

_,mask= cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)# 5x5 kernel with full of ones. 


#all morhological opr
e = cv2.erode(mask,kernel) 
d = cv2.dilate(mask,kernel)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
c= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)   #diff b/w mask and opening
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #diff b/w dilation and erosion
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)  

#display all the result

cv2.imshow("img",img) 
cv2.imshow("mask==",mask)
cv2.imshow("erosion==",e)
cv2.imshow("dilate==",d)
cv2.imshow("opening==",o)
cv2.imshow("closing",c) 
cv2.imshow("x1",x1) 
cv2.imshow("x2",x2) 
cv2.imshow("x3",x3) 

titles = ['image', 'mask', 'erosion', 'dilation', 'opening', 'closing', 
          'x1', 'x2',"x3"]
images = [img,mask,e,d,o,c,x1,x2,x3]

#if you want then plot it
from matplotlib import pyplot as plt
for i in range(9):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


cv2.waitKey(0)
cv2.destroyAllWindows()



