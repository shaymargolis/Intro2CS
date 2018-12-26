#############################################################
# FILE : largest_and_smallest.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex2 2018-2019
# DESCRIPTION : Contains function that returns the maximum
#               And minimum of three numbers
#############################################################


def largest_and_smallest(a, b, c):
    maxi = a
    mini = a

    if b > maxi:
        maxi = b
    if c > maxi:
        maxi = c

    if b < mini:
        mini = b
    if c < mini:
        mini = c

    return maxi, mini


