"""
@author: Osama Shakeel
Image blending project

"""

import cv2
import numpy as np

img1 = cv2.imread("D://music//roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread("D://music//bro_thor.jpg")
img2 = cv2.resize(img2,(500,700))
#cv2.imshow("thor", img1)
#cv2.imshow("bro-thor", img2)

def blend(x):
    pass

img = np.zeros((400,400,3), np.uint8)
cv2.namedWindow("win") #Create track bar windows
cv2.createTrackbar("alpha", "win", 1,100, blend)
switch = "0: Off \n 1: On" #Create switch to invoke track bar
cv2.createTrackbar(switch, "win", 0,1, blend) #Create track bar for switch

while True:
    s= cv2.getTrackbarPos(switch, "win")
    a= cv2.getTrackbarPos("alpha", "win")
    n = (a/100)
    print(n)
    
    if s==0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,1-n, img2,n,0)
        cv2.putText(dst, str(a), (20,50),cv2.FONT_ITALIC,2,(124,266,45), 4)
    cv2.imshow("dst",dst)   
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()