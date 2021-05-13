import random

import cv2,cvzone,keyboard
#cv2 => Computer Vision
#cvzone => For Computer Vision Zone of detectors
#Keybhoard => Takes Input from keyboard
vid=cv2.VideoCapture(0)
detector=cvzone.HandDetector(maxHands=1,detectionCon=0.7)
donecanbepressed,nextcanbepressed=True,False
chanceslist=[[1, 0, 0, 0, 1], [0, 1, 0, 0, 0],
             [0, 1, 1, 0, 1], [0, 0, 1, 0, 0],
             [1, 0, 0, 0, 0], [0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1], [1, 1, 0, 0, 0],
             [1, 1, 1, 0, 0], [0, 0, 0, 1, 1],
             [1, 1, 0, 1, 0], [1, 0, 0, 1, 1],
             [0, 0, 1, 1, 1], [1, 0, 1, 0, 1],
             [1, 0, 1, 1, 0], [1, 0, 0, 1, 0],
             [0, 1, 1, 0, 0],
             [0, 1, 0, 0, 1], [0, 0, 1, 0, 1],
             [0, 0, 1, 1, 0], [0, 0, 0, 1, 0],
             [0, 1, 0, 1, 1], [1, 1, 1, 0, 1],
             [0, 1, 1, 1, 0], [1, 1, 0, 1, 1],
             [1, 1, 1, 1, 0], [1, 1, 0, 0, 1],
             [0, 0, 0, 0, 1], [1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0], [1, 1, 1, 1, 1]]
userchanceslist=[]
fixed=[]
isuserbatting=True


def checkforwin(complist,userlist,isuserbatting):
    if isuserbatting and complist==userlist:
        print("You are Out. Now It's Your balling")
        print(userlist,complist)
        isuserbatting=False
    elif isuserbatting!=True and complist==userlist:
        print("Computer Out. Now It's your batting")
        print(userlist,complist)

        isuserbatting=True
    else:
        print(userlist,complist)#We will Increase Points
    nextcanbepressed=True
    return isuserbatting,nextcanbepressed
def maxchance(ulist):
    li=ulist[0]
    linum=ulist.count(li)
    for i in ulist:
        if ulist.count(i)>linum:
            li=i
    return li
def minchance(ulist):
    li=ulist[0]
    linum=ulist.count(li)
    for i in ulist:
        if ulist.count(i)>linum:
            li=i
    return li
while True:
    success, img=vid.read()
    img=cv2.flip(img,flipCode=1)
    imgframe=img[50:450,100:550]
    img=cv2.rectangle(img,(100,50),(550,450),(0,255,0),3)
    imgframe=detector.findHands(imgframe)
    lmlist,bbox=detector.findPosition(imgframe)
    if keyboard.is_pressed('d') and donecanbepressed:
        if lmlist:
            donecanbepressed=False
            fingers_l=detector.fingersUp()
            fixed=fingers_l
            userchanceslist.append(fixed)
            if len(userchanceslist)>3:
                computermove=maxchance(userchanceslist)
            else:
                computermove=random.choice(chanceslist)
            isuserbatting,nextcanbepressed=checkforwin(computermove,fixed,isuserbatting)
            print(fingers_l)
    if keyboard.is_pressed('n') and nextcanbepressed:
        donecanbepressed=True
        nextcanbepressed=False

    cv2.imshow("ImageFrame",imgframe)
    #cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
