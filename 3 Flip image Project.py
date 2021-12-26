
"""

@author: Osama Shakeel

"""

import cv2

path = input("Enter your image Path: \n") # i.e: D:\\music\\ava.jpg  
print("The path you entered is == ", path)

#Now Read Image

img = cv2.imread(path,0)  #Convert image to Gray Scale Image
img = cv2.resize(img, (760,540))
img = cv2.flip(img, 1) #it accept three parameter 1,0,-1

cv2.imshow("Flip image ", img)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""
#If you want to save the image than
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("D://music//avagrayflip.jpg", img)
else:
    cv2.destroyAllWindows()

"""