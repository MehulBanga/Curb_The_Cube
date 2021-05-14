# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:52:38 2021

@author: mehul
"""
import cv2 as cv
import numpy as np

#Global Variables

Scanned_faces = []
solution = []
step_by_step_solution = False
font = cv.FONT_HERSHEY_TRIPLEX            
font2 = cv.FONT_HERSHEY_COMPLEX_SMALL
blank_preview = np.zeros((600,650,3),np.uint8)