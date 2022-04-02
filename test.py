import cv2
import time
from datetime import datetime, timedelta
global hrs
global mins
global secs
global totalsecs
print('Set the countdown timer:')
hrs = 0
mins = 5
totalsecs = 3600 * hrs + 30 * mins  
cap = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter('video.avi', fourcc, 30.0, (640,480))


while totalsecs != 0:
    sec = timedelta(seconds=int(totalsecs))
    d = datetime(1, 1, 1) + sec
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    videoWriter.write(gray)
    cv2.imshow('frame',frame)
    cv2.putText(frame, str(totalsecs), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text
    totalsecs -= 1
    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"): # quit all
        break
    if totalsecs == 0:
        break
cap.release()
if totalsecs == 0:
    print('Tadaa')
 
 



 

