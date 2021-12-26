"""

@author: Osama Shakeel
Capture Video from Webcam and save in Memory

"""

import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print("cap", cap)

while cap.isOpened:
     ret, frame = cap.read()
     frame = cv2.resize(frame,(700,450))
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     cv2.imshow("frame", frame)
     cv2.imshow("gray", gray)
     k = cv2.waitKey(25) & 0xFF
     if k == ord("q"):
         break
    
cap.release()
cv2.destroyAllWindows()