import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random

cap=cv2.VideoCapture(0)
cap.set(3,360)
cap.set(4,480)
#3 is for width and 4 for height

detector=HandDetector(maxHands=1)
timer=0
gameStarter=False
stateResult=False
scores=[0,0]
playersShows=0

while True:
    imgB=cv2.imread("Resources/BG.png")
    success,img=cap.read()
    imgScaled=cv2.resize(img,(0,0),None,0.875,0.875)#420/480=0.875
    imgScaled=imgScaled[:,80:480]
    
    hands,img=detector.findHands(imgScaled)
    #if hands are found value of hands will be True
    imgB[233:653,795:1195]=imgScaled
    if gameStarter:
        if stateResult is False:
            timer=time.time()-initialTime
            cv2.putText(imgB,str(int(timer)),(598,432),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),4)
            
            if timer>=3:
                timer=0
                stateResult=True  
                if hands:
                    hand=hands[0]
                    fingers=detector.fingersUp(hand)
                    #print(fingers)
                    if fingers==[0,0,0,0,0]:
                        playersShows=1
                    elif fingers==[0,1,1,0,0]:
                        playersShows=3
                    elif  fingers==[0,1,1,0,0]: 
                         playersShows=2
                    randomNumber=random.randint(1,3)     
                    imgAI=cv2.imread(f'Resources/{randomNumber}.png',cv2.IMREAD_UNCHANGED)

                    if (playersShows == 1 and randomNumber == 3) or \
                            (playersShows == 2 and randomNumber == 1) or \
                            (playersShows == 3 and randomNumber == 2):
                        scores[1] += 1
 
                    # AI Wins
                    if (playersShows == 3 and randomNumber == 1) or \
                            (playersShows == 1 and randomNumber == 2) or \
                            (playersShows == 2 and randomNumber == 3):
                        scores[0] += 1
                            
    if stateResult:
        imgB=cvzone.overlayPNG(imgB,imgAI,(149,310)) 

        cv2.putText(imgB, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(imgB, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        

        
    #imgB[233:653,795:1195]=imgScaled
    #cv2.imshow("Image",img)
    cv2.imshow("BG",imgB)
    #cv2.imshow("Scaled",imgScaled)  
    key=cv2.waitKey(1)
    if key==ord('s'):
        gameStarter=True
        initialTime=time.time()
        stateResult=False


