# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:08:03 2021

@author: mehul
"""

import cv2 as cv
from Constants import color_bgr , Symbols
from Variables import blank_preview , font , font2




def draw_instants(frame,cube_instants,face):
    if (face == "current"):
        for x,y in cube_instants[face]:
            cv.rectangle(frame,(x,y),((x+30),(y+30)),(255,255,255),3)
    else:
        for x,y in cube_instants[face]:
            cv.rectangle(frame,(x,y),((x+30),(y+30)),(255,255,255),3)
            
            
def draw_instants_preview(frame,cube_instants):
    faces = ["front","back","up","down","right","left"]
    for face in faces:
        for x,y in cube_instants[face]:
            cv.rectangle(frame,(x,y),(x+40,y+40),(255,255,255),2)
            
def fill_instants(frame,cube_instants,cube):
    for face,colors in cube.items():
        iterator = 0
        for x,y in cube_instants[face]:
            cv.rectangle(frame,(x,y),(x+40,y+40),color_bgr[colors[iterator]],-1)
            iterator+=1

def Symbols_On_Cube(frame,cube_instants):
        faces = ['front','back','left','right','up','down']
        for face in faces:
            for x,y in cube_instants[face]:
                sym,x1,y1= Symbols[face][0][0],Symbols[face][0][1],Symbols[face][0][2]
                cv.putText(blank_preview, sym, (x1,y1), font,1,(0, 0, 0), 1, cv.LINE_AA)  
                sym,col,x1,y1=Symbols[face][1][0],Symbols[face][1][1],Symbols[face][1][2],Symbols[face][1][3]             
                cv.putText(blank_preview, sym, (x1,y1), font,0.5,col, 1, cv.LINE_AA)  
        

        
def Instructions_On_Frame(frame,Instructions):
    for i in range(len(Instructions)):
        instruction,x1,y1 = Instructions[i][0],Instructions[i][1],Instructions[i][2]
        cv.putText(frame, instruction, (x1,y1), font2,.8,(0, 0, 0),1, cv.LINE_AA)


def show_moves():
    img = cv.imread("assets/cubing-notation.jpg") 
    cv.imshow("Guide for Moves", img)  
    
def change_res(width,height,cap):
    cap.set(3,width)
    cap.set(4,height)