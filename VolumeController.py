import cv2 as cv
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
import pycaw  #Allow to manage volume control

###################
wCam,hCam=640,480  #Width of cam,Height of cam

###################
pTime=0
vol=0
volBar=400
volPer=0

cap=cv.VideoCapture(0)

cap.set(3,wCam)
cap.set(4,hCam)

detector=htm.handDetector(detectionCon=0.7)


devices=AudioUtilities.GetSpeakers()
interface=devices.Activate(IAudioEndpointVolume._iid_,
                           CLSCTX_ALL,None)
volume=cast(interface,POINTER(IAudioEndpointVolume))
volume.GetVolumeRange()
volRange=volume.GetVolumeRange()  #OP-(-65.25, 0.0)

minVol=volRange[0]
maxVol=volRange[1]


while True:
    session,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    #print(lmList)
    #IF you want print exact hand number
    if len(lmList)!=0:
        #print(lmList[4],lmList[8])

        x1,y1=lmList[4][1],lmList[4][2]
        x2,y2=lmList[8][1],lmList[8][2]
        cx, cy=(x1+x2)//2,(y1+y2)//2

        cv.circle(img,(x1,y1),15,(255,0,255),cv.FILLED)
        cv.circle(img,(x2,y2),15,(255,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv.circle(img,(cx, cy),15,(255,0,255),cv.FILLED)

        length=math.hypot((x2-x1),(y2-y1))
        #print(length)

        #handrange 50 - 300
        #Volumerange -65-0

        vol=np.interp(length,[50,300],[minVol,maxVol])
        volBar=np.interp(length,[50,300],[400,150])
        volPer=np.interp(length,[50,300],[0,100])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)  # Volume will increase we can also set number as well

        if length<50:
            cv.circle(img,(cx,cy),15,(0,255,0),cv.FILLED)

    cv.rectangle(img,(50,150),(85,400),(255,0,0),3)  #HEight
    cv.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv.FILLED) #Width
    cv.putText(img, f'{int(volPer)}%', (40, 450), cv.FONT_ITALIC,
               1, (0, 255, 255), 2)                                    #percentage


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv.putText(img,f'FPS: {int(fps)}',(40,50),cv.FONT_ITALIC,
               1,(0,255,0),2)

    cv.imshow("Image",img)

    cv.waitKey(1)