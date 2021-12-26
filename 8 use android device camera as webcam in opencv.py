"""
@author: Osama Shakeel
Use android device camera as webcam in opencv

"""
import cv2

#Accessing camera 
camera = "https://192.168.10.8:8080/video"
#Connect your laptop and android device with same network

cap = cv2.VideoCapture(0,  cv2.CAP_DSHOW)

cap.open(camera)
print("Camera ", cap.isOpened())

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("D:\\music\\ipcam.avi", fourcc, 20.0, (760,480))
#output = cv2.VideoWriter("D://ooutput.avi",fourcc,20.0,(640,480),0)
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        frame= cv2.resize(frame,(760,480))
        #gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Gray Frame",gray)
        cv2.imshow("Color frame",frame)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
#Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()