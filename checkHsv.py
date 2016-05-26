import random
import os
import cv2
import numpy as np

from modules import Screenshot
from modules import  RS

rsx, rsy = RS.position()
def TakeScr():
    global rsx
    global rsy

    x1 = rsx + 13
    y1 = rsy + 60 
    x2 = rsx + 500
    y2 = rsy + 352


    play_window = Screenshot.shoot(x1,y1,x2,y2, 'hsv')
    #cv2.imwrite('bankchest.png',play_window)
    #play_window = cv2.imread('bankchest.png',-1)
    #finds red shades
    lower_red = np.array([50,0,50])
    upper_red = np.array([150,30,150])

    mask = cv2.inRange(play_window, lower_red, upper_red)
    mask2 = cv2.inRange(play_window, lower_red, upper_red)
    res = cv2.bitwise_and(play_window, play_window, mask=mask)
    #cv2.imshow('res', res)

    # finds contours of image
    image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Finds contours with edges higher than 4 that make a square
    for i,cnt in enumerate(contours):
        # only gets the biegest contour
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if len(approx)==4 and len(cnt) > 4:
            cv2.drawContours(play_window,[cnt], 0,(0,0,0),-1)
            while True:
                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    break
                cv2.imshow('mask', play_window)

    #cnt = contours[0]
    #print(contours[1])
    #x, y, w, h = cv2.boundingRect(cnt)
    #w = w/2
    #h = h/2
    #x += w/2
    #y += h/2
    # Draws rectangle around it
    #img = cv2.rectangle(mask, (x,y), (x+w, y+h), (0,0,0), 2)
    #gen random coords within bound
    while True:
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        cv2.imshow('mask', mask2)
        #cv2.imshow('res', res)
        #cv2.imshow('play',play_window)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()

TakeScr()
