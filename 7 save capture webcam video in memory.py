"""

@author: Osama Shakeel
Capture Video from Webcam and save in Memory

"""
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# XVID, DVIX, MJPG, X264, WMV1, WMV2 (video formats)

fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("D:\\music\\webcamera.avi",fourcc,20.0,(640,480))
while cap.isOpened:
     ret, frame = cap.read()
     if ret == True:
         #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         #frame = cv2.flip(frame, 0) #for fliping
         cv2.imshow("frame", frame) 
         #cv2.imshow("gray", gray) #for gray frame
         output.write(frame)
         #output.write(gray) #for gray frame
         if cv2.waitKey(1) & 0xFF == ord("q"):
             break
             
    
cap.release()
output.release()
cv2.destroyAllWindows()
