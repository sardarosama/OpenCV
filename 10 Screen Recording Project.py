"""
@author: Osama Shakeel
Screen Recorder ---

"""
import cv2 as c
import pyautogui as p 
import numpy as np

#Create Resolution
rs = p.size()
#Filename to store recording
#fn = input("Enter your path of video storage: \n")

fps = 20.0

fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter("D://musicrec.mp4", fourcc, fps, (780,480))

#Create Recording module

c.namedWindow("Live Reccording", c.WINDOW_NORMAL)
c.resizeWindow("Live Reccording", (760,480))

while True:
    img = p.screenshot()
    frame = np.array(img)
    frame = c.cvtColor(frame, c.COLOR_BGR2RGB)
    output.write(frame)
    c.imshow("Live Recording",frame)
    
    if c.waitKey(1) & 0xFF == ord("q"):
        break
output.release()
c.destroyAllWindows()
