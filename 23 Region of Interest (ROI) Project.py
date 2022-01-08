"""
@author: Osama Shakeel
Region of Interest (ROI) Project ---

"""
import cv2

#read
img = cv2.imread("D://music//roi_opr.jpg")
img = cv2.resize(img,(800,800)) #Width, Height

roi = img[50:205,320:440]

#ironman
img1 = cv2.imread("D://music//ironman.jpg")
img1 = cv2.resize(img1, (900,600))
img1[1:156,560:680] = roi

cv2.imshow("res", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()