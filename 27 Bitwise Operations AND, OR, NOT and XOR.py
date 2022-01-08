"""
@author: Osama Shakeel
Bitwise Operations includes AND, OR, NOT and XOR 
It is most important and use for various purpose like masking
and find roi(region of intereset) which is in complex shape.

"""
import cv2
import numpy as np

img1 = np.zeros((240,400,3), np.uint8)
img1 = cv2.rectangle(img1, (150,100), (200,240),(255,255,255),-1)

img2 = np.zeros((240,400,3), np.uint8)
img2 = cv2.rectangle(img2, (10,10), (170,190),(255,255,255),-1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

#Bitwise AND
bitAnd = cv2.bitwise_and(img2,img1)
cv2.imshow("bitand", bitAnd)

#Bitwise AND
bitOr = cv2.bitwise_or(img2,img1)
cv2.imshow("bitor", bitOr)

#Bitwise NOT
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)
cv2.imshow("bitnot1", bitNot1)
cv2.imshow("bitnot2", bitNot2)

#Bitwise XOR
bitXor = cv2.bitwise_xor(img1,img2)
cv2.imshow("bitXOR", bitXor)


cv2.waitKey(0)
cv2.destroyAllWindows
