# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:51:17 2021

@author: mehul
"""

from Constants import cube , cube_instants
import cv2 as cv
from Variables import blank_preview,font
from Variables import solution
from Graphics import fill_instants

#Visualize these rotations with a real 3*3 cube in hand.

def face_rotate(face):
    main=cube[face]
    front=cube['front']
    left=cube['left']
    right=cube['right']
    up=cube['up']
    down=cube['down']
    back=cube['back']
    
    if face=='front':
        left[2],left[5],left[8],up[6],up[7],up[8],right[0],right[3],right[6],down[0],down[1],down[2]=down[0],down[1],down[2],left[8],left[5],left[2],up[6],up[7],up[8],right[6],right[3],right[0] 
    elif face=='up':
        left[0],left[1],left[2],back[0],back[1],back[2],right[0],right[1],right[2],front[0],front[1],front[2]=front[0],front[1],front[2],left[0],left[1],left[2],back[0],back[1],back[2],right[0],right[1],right[2]
    elif face=='down':
        left[6],left[7],left[8],back[6],back[7],back[8],right[6],right[7],right[8],front[6],front[7],front[8]=back[6],back[7],back[8],right[6],right[7],right[8],front[6],front[7],front[8],left[6],left[7],left[8]
    elif face=='back':
        left[0],left[3],left[6],up[0],up[1],up[2],right[2],right[5],right[8],down[6],down[7],down[8]=up[2],up[1],up[0],right[2],right[5],right[8],down[8],down[7],down[6],left[0],left[3],left[6] 
    elif face=='left':
        front[0],front[3],front[6],down[0],down[3],down[6],back[2],back[5],back[8],up[0],up[3],up[6]=up[0],up[3],up[6],front[0],front[3],front[6],down[6],down[3],down[0],back[8],back[5],back[2]
    elif face=='right':
        front[2],front[5],front[8],down[2],down[5],down[8],back[0],back[3],back[6],up[2],up[5],up[8]=down[2],down[5],down[8],back[6],back[3],back[0],up[8],up[5],up[2],front[2],front[5],front[8]

    main[0],main[1],main[2],main[3],main[4],main[5],main[6],main[7],main[8]=main[6],main[3],main[0],main[7],main[4],main[1],main[8],main[5],main[2]

def face_rotate_ccw(face):
    main=cube[face]
    front=cube['front']
    left=cube['left']
    right=cube['right']
    up=cube['up']
    down=cube['down']
    back=cube['back']
    
    if face=='front':
        left[2],left[5],left[8],up[6],up[7],up[8],right[0],right[3],right[6],down[0],down[1],down[2]=up[8],up[7],up[6],right[0],right[3],right[6],down[2],down[1],down[0],left[2],left[5],left[8]
    elif face=='up':
        left[0],left[1],left[2],back[0],back[1],back[2],right[0],right[1],right[2],front[0],front[1],front[2]=back[0],back[1],back[2],right[0],right[1],right[2],front[0],front[1],front[2],left[0],left[1],left[2]
    elif face=='down':
        left[6],left[7],left[8],back[6],back[7],back[8],right[6],right[7],right[8],front[6],front[7],front[8]=front[6],front[7],front[8],left[6],left[7],left[8],back[6],back[7],back[8],right[6],right[7],right[8]
    elif face=='back':
        left[0],left[3],left[6],up[0],up[1],up[2],right[2],right[5],right[8],down[6],down[7],down[8]=down[6],down[7],down[8],left[6],left[3],left[0],up[0],up[1],up[2],right[8],right[5],right[2] 
    elif face=='left':
        front[0],front[3],front[6],down[0],down[3],down[6],back[2],back[5],back[8],up[0],up[3],up[6]=down[0],down[3],down[6],back[8],back[5],back[2],up[6],up[3],up[0],front[0],front[3],front[6]
    elif face=='right':
        front[2],front[5],front[8],down[2],down[5],down[8],back[0],back[3],back[6],up[2],up[5],up[8]=up[2],up[5],up[8],front[2],front[5],front[8],down[8],down[5],down[2],back[6],back[3],back[0]

    main[0],main[1],main[2],main[3],main[4],main[5],main[6],main[7],main[8]=main[2],main[5],main[8],main[1],main[4],main[7],main[0],main[3],main[6]



def algorithm(moves):
    
    move_symbol = {
        
            "F" : [face_rotate,"front"],
            "F2" : [face_rotate,"front","front"],
            "F'" : [face_rotate_ccw,"front"],
            
            "U" : [face_rotate,"up"],
            "U2" : [face_rotate,"up","up"],
            "U'" : [face_rotate_ccw,"up"],
            
            "D" : [face_rotate,"down"],
            "D2" : [face_rotate,"down","down"],
            "D'" : [face_rotate_ccw,"down"],
            
            "R" : [face_rotate,"right"],
            "R2" : [face_rotate,"right","right"],
            "R'" : [face_rotate_ccw,"right"],
            
            "L" : [face_rotate,"left"],
            "L2" : [face_rotate,"left","left"],
            "L'" : [face_rotate_ccw,"left"],
            
            "B" : [face_rotate,"back"],
            "B2" : [face_rotate,"back","back"],
            "B'" : [face_rotate_ccw,"back"]
            
        }
    
    
    iter = 0
    for move in moves:
        for j in range(len(move_symbol[move]) - 1):
            move_symbol[move][0](move_symbol[move][j+1])
                
        cv.putText(blank_preview,move,(600,iter+50),font,1,(0,255,0),1,cv.LINE_AA)
        fill_instants(blank_preview,cube_instants,cube)
        solution.append(blank_preview)
        cv.imshow("Solution", blank_preview)
        cv.waitKey()
        cv.putText(blank_preview,move,(600,50),font,1,(0,0,0),1,cv.LINE_AA)
