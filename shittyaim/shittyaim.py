import cv2
import numpy as np
from PIL import ImageGrab
from time import time
from pynput import mouse
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()

hL = ()
sL = ()
vL = (20)
hH = ()
sH = ()
vH = (255)
cLen = (500)

userBoss = str(input("Insert Boss Here: "))

if userBoss == ('King Slime') or userBoss == ('1'):
    hL = (110)
    sL = (150)
    hH = (130)
    sH = (255)
elif userBoss == ('Eye of Cthulhu') or userBoss == ('2'):
    hL = (0)
    sL = (150)
    hH = (8)
    sH = (255)
    cLen = (200)
elif userBoss == ('Queen Bee') or userBoss == ('3'):
    hL = (15)
    sL = (150)
    hH = (35)
    sH = (255)
    clen = (100)
elif userBoss == ('Skeletron') or userBoss == ('4'):
    hL = (10)
    sL = (0)
    hH = (40)
    sH = (100)
elif userBoss == ('Deerclops') or userBoss == ('5'):
    hL = (110)
    sL = (150)
    hH = (130)
    sH = (255)
elif userBoss == ('Wall of Flesh') or userBoss == ('6'):
    hL = (0)
    sL = (150)
    hH = (5)
    sH = (255)
elif userBoss == ('Queen Slime') or userBoss == ('7'):
    hL = (130)
    sL = (75)
    hH = (150)
    sH = (255)
elif userBoss == ('The Twins') or userBoss == ('8'):
    hL = (0)
    sL = (150)
    hH = (8)
    sH = (255)
    vL = (100)
elif userBoss == ('The Destroyer') or userBoss == ('9'):
    hL = (170)
    sL = (100)
    hH = (180)
    sH = (255)
    cLen = (10)
elif userBoss == ('Skeletron Prime') or userBoss == ('10'):
    hL = (0)
    sL = (100)
    hH = (10)
    sH = (255)
    cLen = (2)
elif userBoss == ('Plantera') or userBoss == ('11'):
    hL = (150)
    sL = (150)
    hH = (170)
    sH = (255)
    cLen = (100)
elif userBoss == ('Empress of Light') or userBoss == ('12'):
    hL = (25)
    sL = (75)
    hH = (35)
    sH = (255)
    cLen = (100)
elif userBoss == ('Moon Lord') or userBoss == ('13'):
    hL = (75)
    sL = (75)
    hH = (95)
    sH = (255)
    cLen = (20)    
loop_time = time()
while(True):

    display = ImageGrab.grab(bbox=(150, 150, 1920, 950))
    display = np.array(display) #converting to format that opencv understands (PIL to opencv)
    display = display[:, :, ::-1].copy() #converts RGB to BGR, OpenCV likes BGR :D

    hsv = cv2.cvtColor(display, cv2.COLOR_BGR2HSV) #converts BGR to HUE SATURATION AND BRIGHTNESS
    lower = np.array([hL, sL, vL])
    upper = np.array([hH, sH, vH])

    mask = cv2.inRange(hsv, lower, upper)

    contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > cLen:
               x, y, w, h = cv2.boundingRect(contour) 
               cv2.rectangle(display, (x,y), (x + w, y + h), (0, 0, 255), 3)
               M = cv2.moments(contour)

               cx = int(M["m10"] / M["m00"])
               cy = int(M["m01"] / M["m00"])

               cv2.circle(display, (cx, cy),7,(0, 255, 0), -1)
               centerX = (cx)
               centerY = (cy)
               center = (cx, cy)
               print (center)
               mouse.position = (centerX+150, centerY+150)

    cv2.namedWindow('Original_Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Masked_Image', cv2.WINDOW_NORMAL)
    cv2.moveWindow('Original_Image', 40,30)

    cv2.resizeWindow('Original_Image', 960, 540)
    cv2.resizeWindow('Masked_Image', 480, 270)

    cv2.imshow('Masked_Image', mask) #masked
    cv2.imshow('Original_Image', display) #original

    cv2.waitKey(1)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done')