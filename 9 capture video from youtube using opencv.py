"""
@author: Osama Shakeel
Capture Video from Youtube

"""
import cv2
import pafy
url = "https://www.youtube.com/watch?v=jwZXcnh3Duo"
data = pafy.new(url)
data = data.getbest(preftype = "mp4")
cap = cv2.VideoCapture(0,  cv2.CAP_DSHOW)

cap.open(data.url)
print("Video == ", cap.isOpened())


while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        frame= cv2.resize(frame,(760,480))
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Frame",gray)
        cv2.imshow("Color frame",frame)
        cv2.imshow("Gray Frame",gray)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
#Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

#if any os error regarding youtube-dl occur thn
#conda install -c forge youtube-dl
#pip3 install youtube-dl

