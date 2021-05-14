# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:24:39 2021

@author: mehul
"""

def is_between(x,a,b):
    if(a <= x <= b):
        return True
    else:
        False


#HSV of Colors
# green [[[ 60 255 255]]]
# red [[[  0 255 255]]]
# blue [[[120 255 255]]]
# white [[[  0   0 255]]]
# yellow [[[ 30 255 255]]]
# orange [[[ 15 255 255]]]


def color_detect(h,s,v):
    if (h <= 7 or is_between(h, 160, 190)) and s > 100:
        return "red"
    elif is_between(h, 40 ,100 ) and s > 70 and v >100:
        return"green"
    elif is_between(h,100 ,140) and s>70:
        return"blue"
    elif is_between(h,20,40 )and s >70 :
        return"yellow"
    elif is_between(h,7 ,20 ) and s>70 :
        return"orange"
    elif h<=15 and s<70 and v<=255:
        return "white"
    
    return "white"