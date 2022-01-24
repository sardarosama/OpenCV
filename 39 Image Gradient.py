
import cv2
import numpy as np


img = cv2.imread("D:\\music\\sam.jpeg")  
img = cv2.resize(img,(400,400))
cv2.imshow("original==",img)
#define a kernal for homogeneous function
kernel = np.ones((5,5),np.float32)/25

h_filter = cv2.filter2D(img,-1,kernel) # -1 is desired depth
gau= cv2.GaussianBlur(img,(5,5),0) #here 0 is sigma x value
cv2.imshow("gau blur=",gau)

med = cv2.medianBlur(img,5)
cv2.imshow("median filter",med)
bi_f = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bi_f",bi_f)
blur = cv2.blur(img,(8,8)) #here we have image and kernel as parameter
cv2.imshow("blur==",blur)
cv2.imshow("homogeneous==",h_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()
