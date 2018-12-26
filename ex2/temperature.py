#############################################################
# FILE : temperature.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex2 2018-2019
# DESCRIPTION : Contains function to determine if it is
#               summer based on temperature of last 3 days
#############################################################


def is_it_summer_yet(x, t1, t2, t3):
    """
        Returns true if atleast two from three
        temperature measurements t1, t2, t3
        are higher than x.
    """

    above_max = 0

    if t1 > x:
        above_max += 1

    if t2 > x:
        above_max += 1

    if t3 > x:
        above_max += 1

    return above_max >= 2

