"""
@author = Osama Shakeel

     -------------Morphological Transformations-----------------------

Morphological transformations are some simple operations based on the image shape.
It is normally performed on binary images. 
It needs two inputs, 1)- original image, 2)- structuring element(kernel).
Two more basic Morphological Transformations are 
1) - Opening and 2) - Closing

"""
import cv2
import numpy as np



img = cv2.imread('D:\\music\\col_balls.jpg',0)
_,mask= cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)

cv2.imshow("img",img) 
cv2.imshow("mask==",mask)

"""
Opening --
Opening is just another name of erosion followed by dilation. 
means first erosion take place then dilation

"""

kernel = np.ones((3,3),np.uint8)# 5x5 kernel with full of ones. 
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #optional parameters iterations = 2

cv2.imshow("ker=",kernel)
cv2.imshow("opening==",o)

"""
closing --

It is opposite of opening
closing is just another name of dilation followed by erosion. 
means first dilation take place then erosion-

"""

kernel = np.ones((3,3),np.uint8)# 5x5 kernel with full of ones. 
c= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) #optional parameters iterations = 2
cv2.imshow("closing",c) 


#if you want then plot it
from matplotlib import pyplot as plt
titles = ["img","mask","opening","closing"]
images = [img,mask,o,c]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

#--------Optional ----

x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)   #diff b/w mask and opening
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #diff b/w dilation and erosion
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)  
cv2.imshow("x1",x1) 
cv2.imshow("x2",x2) 
cv2.imshow("x3",x3) 


cv2.waitKey(0)
cv2.destroyAllWindows()

