"""
@author: Osama Shakeel
Image Conversion Project Colored Image to GrayScale Image

"""
import cv2

path = input("Enter your image Path: \n") # i.e: D:\\music\\ava.jpg  
print("The path you entered is == ", path)

#Now Read Image

img = cv2.imread(path,0)  #Convert image to Gray Scale Image
img = cv2.resize(img, (760,540))

cv2.imshow("Converted image ", img)

k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("D://music//avagray.jpg", img)
else:
    cv2.destroyAllWindows()

