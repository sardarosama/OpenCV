"""

@author: Osama Shakeel
Read Video using Opencv

"""

import cv2

cap = cv2.VideoCapture("D://music//hello.mp4")
print("cap", cap)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(700,450))
    cv2.imshow("frame", frame)
    k = cv2.waitKey(25) & 0xFF
    if k == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()