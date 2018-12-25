############################################################
# FILE : special.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the special shot
#############################################################

from element import Element
from torpedo import Torpedo


class Special(Torpedo):
    SPECIAL_SIZE = 4
    SPECIAL_LIFE_TIME = 150

    def __init__(self, position, velocity, angle, ttl=SPECIAL_LIFE_TIME):
        """
        Creates a torpedo class instance
        :param position: position vector (x,y)
        :param velocity: velocity vector (v_x, v_y)
        :param angle: angle in degrees
        :return:
        """
        Torpedo.__init__(self, position, velocity, angle, ttl)

    def get_size(self):
        return self.SPECIAL_SIZE

