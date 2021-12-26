"""
@author: Osama Shakeel
Draw DateTime on video and figure using opencv

"""

import cv2
import datetime
cap = cv2.VideoCapture("D://music//hello.mp4")
print("for width ==", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for heigth ==", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("for width == ", cap.get(3))  #here 3 for width
print("for heigth ==", cap.get(4))  #here 4 for heigth


while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600,700))
    if ret==True:
        
       
       font= cv2.FONT_HERSHEY_COMPLEX_SMALL
       text = "Width: " + str(cap.get(3)) + "Heigth: " + str(cap.get(4))
       frame = cv2.putText(frame, text, (120,120),font,1,(0,155,0),1,cv2.LINE_AA )
       datedata = "date: " + str(datetime.datetime.now())
       frame = cv2.putText(frame, datedata, (140,140),font,1,(120,155,120),1,cv2.LINE_AA )
       cv2.rectangle(frame, (384, 10), (510, 128), (128, 0, 255), 8)
       cv2.imshow("frame", frame)
       if cv2.waitKey(25) & 0xFF == ord("q"):
           break
       
cap.release()
cv2.destroyAllWindows()