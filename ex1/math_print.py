#############################################################
# FILE : math_print.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex1 2018-2019
# DESCRIPTION : A set of function relating to math
#############################################################

import math


def golden_ratio():
    """ calculates and prints the golden ratio """
    print((1 + math.pow(5, 0.5)) / 2)


def six_cubed():
    """ calculates the result of 6 cubed. """
    print(math.pow(6, 3))


def hypotenuse():
    """ calculates the length of the hypotenuse in
        a right triangular with cathuses 5,3 """
    print(math.sqrt(math.pow(5, 2) + math.pow(3, 2)))


def pi():
    """ returns the value of the constant PI """
    print(math.pi)


def e():
    """ returns the value of the constant E """
    print(math.e)


def triangular_area():
    """ prints the areas of the right triangulars with
        equals cathuses with lengths from 1 to 10 """
    print(1*1/2, 2*2/2, 3*3/2, 4*4/2, 5*5/2,
          6*6/2, 7*7/2, 8*8/2, 9*9/2, 10*10/2)