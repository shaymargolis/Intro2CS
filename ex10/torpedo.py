############################################################
# FILE : torpedo.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the torpedo
#############################################################

from element import Element


class Torpedo(Element):

    def __init__(self, position, velocity, angle):
        """
        Creates a torpedo class instance
        :param position: position vector (x,y)
        :param velocity: velocity vector (v_x, v_y)
        :param angle: angle in degrees
        :return:
        """

        Element.__init__(self, position, velocity, angle)