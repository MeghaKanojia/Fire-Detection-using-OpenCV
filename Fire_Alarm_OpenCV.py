import cv2
import numpy as np
import playsound

Fire_reported=0
Alarm_Status = False


def play_audio():
    playsound.playsound('Alarm.mp3',True)
vedio=cv2.VideoCapture('Fire_vedio.mp4')
while True:
    ret, frame=vedio.read()
    frame=cv2.resize(frame,(1000,600))
    blur= cv2.GaussianBlur(frame,(15,15),0)
    hsv= cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower=[18,50,50]
    upper=[35,255,255]

    lower=np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    mask= cv2.inRange(hsv,lower,upper)

    output = cv2.bitwise_and(frame,hsv,mask=mask)

    size = cv2.countNonZero(mask)

    if int(size)>15000:
        Fire_reported+=1

        if Fire_reported>=1:
            if Alarm_Status == False:
                play_audio()
                Alarm_Status = True


    if ret==False:
        break

    cv2.imshow('vedio',output)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cv2.destroyAllWindows()
vedio.release()