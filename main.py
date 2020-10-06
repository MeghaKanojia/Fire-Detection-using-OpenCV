import cv2
import numpy as np
import playsound

Fire_reported=0
Alarm_Status = False

vedio_path=input("Enter anyone vedio path from:\n'Building_Fire.mp4'\n'Fire_vedio.mp4'\n'0 : for accessing camera'\n ") #taking vedio as input from user



if vedio_path=='0':
    vedio = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # object created to capture a vedio
else:
    vedio = cv2.VideoCapture(vedio_path)  # object created to capture a vedio
def play_audio():
    print('Wait for audio to end')
    playsound.playsound('Alarm.mp3',True)       #function is called for turning on alarm, when fire is detected


if not (vedio.isOpened()):
    print('Could not open video device')

while True:
    ret, frame=vedio.read()                     #reading or capturing vedio frame by frame
    #frame=cv2.resize(frame,(1000,500))         #for resizing frame

    font = cv2.FONT_HERSHEY_SIMPLEX

    blur= cv2.GaussianBlur(frame,(15,15),0)     #for removing noise ; Image smoothening
    hsv= cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)  #converting from BGR to HSV

    lower=[25,90,90]                            #lower range for HSV
    upper=[35,255,255]                          #upper range for HSV

    lower=np.array(lower, dtype='uint8')        #converting to numpy array for simplicity
    upper = np.array(upper, dtype='uint8')

    mask= cv2.inRange(hsv,lower,upper)          #creating mask over range of HSV, ranging between lower and upper

    output = cv2.bitwise_and(frame,hsv,mask=mask)
    # putText() method for
    # inserting text on video
    cv2.putText(output, "Detects fire with size>15000 ",
                (25, 25),
                font, 1,
                (24, 49, 49),
                2,
                cv2.LINE_4)
    cv2.putText(output, " Press 'q' to quit vedio window",
                (50, 50),
                font, 1,
                (24, 49, 49),
                2,
                cv2.LINE_4)
    cv2.putText(output, " Wait for alarm to STOP if it is 'on'",
                (75, 75),
                font, 1,
                (24, 49, 49),
                2,
                cv2.LINE_4)

    size = cv2.countNonZero(mask)               #measuring size of fire

    if int(size)>1000:
        Fire_reported+=1

        if Fire_reported>=1:
            if Alarm_Status == False:
                play_audio()
                Alarm_Status = True

    if ret==False:
        break


    cv2.imshow('vedio',output)
    cv2.imshow('original',frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):          #press q to quit vedio window
        break
cv2.destroyAllWindows()
vedio.release()