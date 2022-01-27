"""
@author: Osama Shakeel 

          ---Feature Detection and Description---
          
For understanding  this we recall jisaw puzzle game where we combine multiple 
small pieces in correct order by identifying its corners , shape and pattern.

On the basis of all these we all detect corners in images with so many approaches,

          ---Shi-Tomasi Corner Detector---

We will learn about the another corner detector: Shi-Tomasi Corner Detector
We will see the function: cv2.goodFeaturesToTrack().
Shi- Tomasi approach is more effective as compared with Harris Corner detection

In this we limit the number of corners and corners quality.
It is more user friendly.

"""

import numpy as np
import cv2

img = cv2.imread('D:\\music\\shapes.png')
#image must be in gary
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#parameters (img,no.of corner,quality_level,min_distance between corner)
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("res==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
