"""

@author: Osama Shakeel
Convert Video Color Frame to Gray

"""

import cv2

cap = cv2.VideoCapture("D://music//hello.mp4")
print("cap", cap)

while True:
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