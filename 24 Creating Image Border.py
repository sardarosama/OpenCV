"""
@author: Osama Shakeel
Creating Image Border --->
With the help of cv2.copyMakeBorder() function
It takes four parameters like (img, border_width(4-sides), bordertype, val_border )
Border width = top, bottom, right,left
"""
import cv2

#read
img = cv2.imread("D://music//lion.jpg")
img = cv2.resize(img, (1000,600))
#Creating Image Border
brdr = cv2.copyMakeBorder(img, 10,10,15,15, cv2.BORDER_CONSTANT, value = [255,134,24])

cv2.imshow("res", brdr)

cv2.waitKey(0)
cv2.destroyAllWindows()