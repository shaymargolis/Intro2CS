#############################################################
# FILE : shapes.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex2 2018-2019
# DESCRIPTION : Contains function to calculate area of
#               different shapes from user input
#############################################################

import math


def shape_area():
    """

    """
    shape = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")

    if shape == '1':
        radius = input()
        return float(radius)*float(radius)*math.pi

    if shape == '2':
        a = float(input())
        b = float(input())
        return a*b

    if shape == '3':
        a = float(input())
        return (math.sqrt(3)/4)*(a*a)
