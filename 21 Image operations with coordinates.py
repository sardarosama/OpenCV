"""
@author: Osama Shakeel
Image Operations with coordinates ---

"""
import cv2

img = cv2.imread("D://music//lion.jpg")
img = cv2.resize(img, (1024,700))
cv2.imshow("res", img)
print("Shape == ", img.shape) # Return a tuple of numbers of rows, columns
print("No of Pixels ==", img.size) # Return Total numbers of pixels
print("Datatype ==", img.dtype) #Return image datatype
print("Image Type== ", type(img))

#Access a pixel value by its row and column coordinate
px = img[520,580] #Store coordinate in variable
print("The pixels of coordinates are ",  px)
#Now try to find selected channel value by its row and column coordinates
#We know we have three channels - 0,1,2 (bgr)
#Accessing only blue pixel

blue = img[520,580,0]
print("Blue color pixel is ", blue)

green = img[520,580,1]
print("Green color pixel is ", green)

red = img[520,580,2]
print("Red color pixel is ", red)



cv2.waitKey(0)
cv2.destroyAllWindows()