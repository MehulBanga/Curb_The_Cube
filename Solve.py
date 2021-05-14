# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:27:53 2021

@author: mehul
"""
import kociemba 
from Constants import Face_Assignment


#Using Kociemba's python library to solve rubix cube efficiently
def solve(cube):
    unsolved_cube = ""
    for face in cube:
        for piece in cube[face]:
            unsolved_cube += Face_Assignment[piece]
    step_by_step_solution = kociemba.solve(unsolved_cube)
    print("Steps to Solve cube : ", step_by_step_solution)
    return step_by_step_solution