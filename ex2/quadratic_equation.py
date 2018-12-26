#############################################################
# FILE : quadratic_equation.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex2 2018-2019
# DESCRIPTION : Contains functions to calculate result of
#               Quadratic equations
#############################################################

import math


def quadratic_equation(a, b, c):
    """
        Solves quadratic equation, with the
        parameters a,b,c. If there are 2 solutions,
        It returns them. If there is 1 solution, it
        returns it and None. If there is no solution
        at all, it returns None and None.
    """
    det = b*b - 4*a*c

    if det < 0:
        #  If the determinant is less than zero,
        #  There are no solutions
        return None, None
    elif det == 0:
        #  If the determinant is zero,
        #  There is only one solution
        x1 = -b/(2*a)
        return x1, None

    #  If the determinant is zero,
    #  There are 2 solutions
    x1 = (-b + math.sqrt(det))/2*a
    x2 = (-b - math.sqrt(det))/2*a
    return x1, x2


def quadratic_equation_user_input():
    """
        Requests quadratic equation parameters from
        input in the format of "(a) (b) (c)", and
        prints the solutions of it.
    """

    #  Get the parameters from input and split to a,b,c
    user_input = input("Insert coefficients a, b, and c: ")
    user_params = user_input.split()

    #  S1 and S2 for Solution1 and Solution2
    s1, s2 = quadratic_equation(float(user_params[0]),
                                float(user_params[1]),
                                float(user_params[2]))

    if s1 == None and s2 == None:
        print("The equation has no solutions")
    elif s1 != None and s2 == None:
        print("The equation has 1 solution:", s1)
    else:
        print("The equation has 2 solutions:", s1, "and", s2)

