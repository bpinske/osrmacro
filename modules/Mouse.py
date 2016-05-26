#!/usr/bin/python2 
import RandTime 
import autopy
import random


"""Module to move mouse"""

def moveTo(x,y):
    """Move mouse  NOT in a straight line"""
    cur_x, cur_y = autopy.mouse.get_pos() #Gets initial mouse location
    #screen_x, screen_y = autopy.screen.get_size() #gets screen size
   
    while True:
        min_x = min(cur_x, x)#Decides minimun X,Y 
        max_x = max(cur_x, x)#Decides maximum X,Y coords

        min_y = min(cur_y, y)
        max_y = max(cur_y, y)
        
        #find furthest distance of X and Y
        len_x = max_x - min_x
        len_y = max_y - min_y

        overshoot = random.randint(0,99)
        #breaks once it's around +-2 pixels around the target area
        if (len_x) <= 2 and  (len_y) <= 2:
            break
#        ############################################ DEBUG ###################################
#        if random.randint(0,4)==0:
#            if cur_x > x:#Higher X
#                cur_x -= random.randint(0,2)
#            else:#Lower x
#                cur_x += random.randint(0,2)
#            #checks if current Y is higher or lower than target Y
#            if cur_y > y: # Higher Y
#                cur_y -= random.randint(0,2)
#            else: #Lower Y
#                cur_y += random.randint(0,2)
#        else:
#
#            if cur_x > x:#Higher X
#                cur_x -= random.randint(0,7)
#            else:#Lower x
#                cur_x += random.randint(0,7)
#            #checks if current Y is higher or lower than target Y
#            if cur_y > y: # Higher Y
#                cur_y -= random.randint(0,7)
#            else: #Lower Y
#                cur_y += random.randint(0,7)
#        if random.randint(0,4) == 0:
#            RandTime.randTime(0,0,1,0,0,1)
#            
#        #####################################################################################
        ##checks if current X is higher or lower than target X
        if cur_x > x:#Higher X
            if len_x > 100:
                cur_x -= random.randint(51,99)
            elif len_x <= 5:
                cur_x -= random.randint(1,3)
                if overshoot == 5:
                    cur_x -= random.randint(1,9)
            elif len_x <= 11:
                cur_x -= random.randint(1,5)
            elif len_x <= 19:
                cur_x -= random.randint(1,9)
            elif len_x <= 50:
                cur_x -= random.randint(5,24)
            elif len_x <= 100:
                cur_x -= random.randint(25,55)

        else:#Lower x
            if len_x > 100:
                cur_x += random.randint(51,99)
            elif len_x <= 5:
                cur_x += random.randint(1,3)
                if overshoot == 7:
                    cur_x += random.randint(1,9)
            elif len_x <= 11:
                cur_x += random.randint(1,5)
            elif len_x <= 19:
                cur_x += random.randint(1,9)
            elif len_x <= 50:
                cur_x += random.randint(5,24)
            elif len_x <= 100:
                cur_x += random.randint(25,55)

        #checks if current Y is higher or lower than target Y
        if cur_y > y: # Higher Y
            if len_y > 100:
                cur_y -= random.randint(51,99)
            elif len_y <= 5:
                cur_y -= random.randint(1,3)
                if overshoot == 7:
                    cur_x -= random.randint(1,9)
            elif len_y <= 11:
                cur_y -= random.randint(1,5)
            elif len_y <= 19:
                cur_y -= random.randint(1,9)
            elif len_y <= 50:
                cur_y -= random.randint(5,24)
            elif len_y <= 100:
                cur_y -= random.randint(25,55)
        else: #Lower Y
            if len_y > 100:
                cur_y += random.randint(51,99)
            elif len_y <= 5:
                cur_y += random.randint(1,3)
                if overshoot == 7:
                    cur_x += random.randint(1,9)
            elif len_y <= 11:
                cur_y += random.randint(1,5)
            elif len_y <= 19:
                cur_y += random.randint(1,9)
            elif len_y <= 50:
                cur_y += random.randint(5,25)
            elif len_y <= 100:
                cur_y += random.randint(25,55)
        
        #print("Moving to {0} {1}".format(cur_x, cur_y))
        if overshoot == 7:
            RandTime.randTime(0,0,1,0,9,9)

        #slows down if closer to target coord
        if (len_x) <= random.randint(1,5) and  (len_y) <= random.randint(1,5):
            RandTime.randTime(0,0,0,0,0,9)
        else:
            if overshoot == 0:
                RandTime.randTime(0,0,0,0,0,2)

        autopy.mouse.smooth_move(cur_x,cur_y)#moves to generated location

        #autopy.mouse.move(cur_x, cur_y)

def click(button):
    #autopy.mouse.click()
    #
    autopy.mouse.toggle(True,button)
    RandTime.randTime(0,0,0,0,0,1)#time between click
    RandTime.randTime(0,0,0,0,0,0)
    autopy.mouse.toggle(False,button)

    RandTime.randTime(0,0,0,0,1,9)

def moveClick(x,y, button=0):#moves to random X,Y of found match of template
    moveTo(x,y)
    RandTime.randTime(0,1,0,0,9,9)
    if button != 0:
        autopy.mouse.toggle(True,button)
        RandTime.randTime(0,0,0,0,0,1)
        RandTime.randTime(0,0,0,0,0,0)
        autopy.mouse.toggle(False,button)
def randCoord(pt,w,h ):
    """Takes a top-left point as pt, and width and height of template
        returns a pair of coordinates within the the size of the template, to be used with inventory bag items only"""
    w = pt[0]+w
    h = pt[1]+h
    print(w)
    print(h)

    x = random.randint(pt[0]+3,(w-3))
    y = random.randint(pt[1]+3,(h-3))
    return x,y

def genCoords(x1,y1,x2,y2):
    """Returns random coords of passed coordinates, not relative to RS window"""
    x = random.randint(x1,x2)
    y = random.randint(y1,x2)
    return x, y



