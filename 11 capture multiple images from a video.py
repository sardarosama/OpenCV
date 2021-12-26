"""
@author: Osama Shakeel
Capture Multiple Images from a video

"""

import cv2

vidcap = cv2.VideoCapture("D://music//hello.mp4")

ret, image = vidcap.read() #Read 
count = 0

while True:
    if ret == True:
        cv2.imwrite("D://avg//imgN%d.jpg " %count, image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count**100))
        ret, image = vidcap.read() 
        cv2.imshow("cap", image)
        print(count)
        
        count += 1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()
        
vidcap.release()
cv2.destroyAllWindows
        


