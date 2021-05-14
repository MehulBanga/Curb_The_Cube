# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:36:50 2021

@author: mehul
"""

import cv2 as cv

from Constants import cube , cube_instants, Instructions, color_bgr
from Variables import Scanned_faces , step_by_step_solution , blank_preview
from Graphics import show_moves , change_res , draw_instants , draw_instants_preview , fill_instants , Symbols_On_Cube , Instructions_On_Frame
from Algorithms import  algorithm
from ColorDetection import color_detect
from Solve import solve



#Live video from webcam
cap = cv.VideoCapture(0)
cv.namedWindow('Frame')




if __name__ == "__main__":
    
    
    change_res(1280,720,cap)
    while True:
        hsv = []
        current_state = []
        ret,img = cap.read()
        Instructions_On_Frame(img, Instructions);

        frame = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        
        draw_instants(img, cube_instants, "main")
        draw_instants(img, cube_instants, "current")
        draw_instants_preview(blank_preview, cube_instants)
        fill_instants(blank_preview, cube_instants, cube)
        Symbols_On_Cube(blank_preview,cube_instants)
        
        for i in range(9):
            hsv.append(frame[cube_instants["main"][i][1]][cube_instants["main"][i][0]])
            
            
        iterator = 0
        for x,y in cube_instants["current"]:
            color_name = color_detect(hsv[iterator][0],hsv[iterator][1],hsv[iterator][2])
            cv.rectangle(img,(x,y),((x+30),(y+30)),color_bgr[color_name],-1)
            iterator+=1
            current_state.append(color_name)
            
            
        k = cv.waitKey(5) & 0xFF
        
        if(k == 27):
            break

#press w to scan upward face
        elif k == ord("w"):
            cube["up"] = current_state
            Scanned_faces.append("w")
            
            
#press d to scan right face            
        elif k == ord("d"):
            cube["right"] = current_state
            Scanned_faces.append("d")
            
            
#press a to scan left face            
        elif k == ord("a"):
            cube["left"] = current_state
            Scanned_faces.append("a")   

#press s to scan downward face            
        elif k == ord("s"):
            cube["down"] = current_state
            Scanned_faces.append("s") 

#press z to scan front face              
        elif k == ord("z"):
            cube["front"] = current_state
            Scanned_faces.append("z") 
  
#press x to scan backward face 
        elif k == ord("x"):
            cube["back"] = current_state
            Scanned_faces.append("x") 
                    
        elif k == ord("\r"):
            if len(set(Scanned_faces)) == 6:
                try:
                    step_by_step_solution = solve(cube)
                    if(step_by_step_solution):
                        moves = step_by_step_solution.split(' ')
                        cv.destroyWindow("Preview")
                        show_moves()
                        algorithm(moves)
                        
                        
                except:
                    print("ERROR while scanning faces")
                    
            else:
                print("all sides not scanned yet")
                print("Faces left :" , 6 - len(Scanned_faces))
            
            
        cv.imshow("Preview", blank_preview)
        cv.imshow("Frame", img)
    cap.release()   
    cv.destroyAllWindows()
