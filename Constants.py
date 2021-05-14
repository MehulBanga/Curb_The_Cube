# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:43:19 2021

@author: mehul
"""

cube = {
        "up" : ["grey","grey","grey","grey","grey","grey","grey","grey","grey"],
        "right" : ["grey","grey","grey","grey","grey","grey","grey","grey","grey"],
        "front" : ["grey","grey","grey","grey","grey","grey","grey","grey","grey"],
        "down" : ["grey","grey","grey","grey","grey","grey","grey","grey","grey"],
        "left" : ["grey","grey","grey","grey","grey","grey","grey","grey","grey"],
        "back" : ["grey","grey","grey","grey","grey","grey","grey","grey","grey"]    
}



cube_instants = {
        "main" : [
            [200,120],  [300,120],  [400,120],
            [200, 220], [300, 220], [400, 220],
            [200, 320], [300, 320], [400, 320]  
        ],
        'current': [
            [20, 20], [54, 20], [88, 20],
            [20, 54], [54, 54], [88, 54],
            [20, 88], [54, 88], [88, 88]
        ],
        'preview': [
            [20, 130], [54, 130], [88, 130],
            [20, 164], [54, 164], [88, 164],
            [20, 198], [54, 198], [88, 198]
        ],
        'left': [
            [50, 280], [94, 280], [138, 280],
            [50, 324], [94, 324], [138, 324],
            [50, 368], [94, 368], [138, 368]
        ],
        'front': [
            [188, 280], [232, 280], [276, 280],
            [188, 324], [232, 324], [276, 324],
            [188, 368], [232, 368], [276, 368]
        ],
        'right': [
            [326, 280], [370, 280], [414, 280],
            [326, 324], [370, 324], [414, 324],
            [326, 368], [370, 368], [414, 368]
        ],
        'up': [
            [188, 128], [232, 128], [276, 128],
            [188, 172], [232, 172], [276, 172],
            [188, 216], [232, 216], [276, 216]
        ],
        'down': [
            [188, 434], [232, 434], [276, 434],
            [188, 478], [232, 478], [276, 478],
            [188, 522], [232, 522], [276, 522]
        ], 
        'back': [
            [464, 280], [508, 280], [552, 280],
            [464, 324], [508, 324], [552, 324],
            [464, 368], [508, 368], [552, 368]
        ],
}


Face_Assignment = {
    'green'   : 'F',
    'yellow'  : 'U',
    'blue'    : 'B',
    'orange'  : 'R',
    'red'     : 'L',
    'white'   : 'D'
}

color_bgr = {
    "red"    : (0,0,204),
    "orange" : (0,128,255),
    "blue"   : (255,0,0),
    "green"  : (0,235,0),
    "white"  : (255,255,255),
    "yellow" : (0,255,255),
    "grey"   : (128,128,128)
}


Symbols = {
    'up'    :   [['W',242, 202],    ['Y',   (0,255,255)  ,      260,208]],
    'right' :   [['D',380, 354],    ['O',   (0,165,255)  ,      398,360]],
    'front' :   [['Z',242, 354],    ['G',   (0,255,0)    ,      260,360]],
    'down'  :   [['S',242, 508],    ['W',   (255,255,255),      260,514]],
    'left'  :   [['A',104, 354],    ['R',   (0,0,255)    ,      122,360]],
    'back'  :   [['X',518, 354],    ['B',   (255,0,0)    ,      536,360]],
    }




Instructions = {
 0 : ["Instructions : ",510,50],
 1 : ["1) Face with Green center-piece is Front face & Red is left.",510,100],
 2 : ["2) Alphabet on center-piece in preview tab is key to capture the face.",510,150],
 3 : ["3) Once, All faces are scanned, press enter/any key to view solution.",510,200],
 4 : ["4) Solution window shows step at Top right corner & live state of cube",510,250],
 5 : ["5) Take help from Guide window to perform moves.",510,300],
 6 : ["6) To exit, Press escape key multiple times.",510,350]    
    }




