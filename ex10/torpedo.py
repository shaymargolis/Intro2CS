############################################################
# FILE : torpedo.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the torpedo
#############################################################

from element import Element


class Torpedo(Element):
    TORPEDO_SIZE = 4
    TORPEDO_LIFE_TIME = 200

    def __init__(self, position, velocity, angle, ttl=TORPEDO_LIFE_TIME):
        """
        Creates a torpedo class instance
        :param position: position vector (x,y)
        :param velocity: velocity vector (v_x, v_y)
        :param angle: angle in degrees
        :return:
        """
        self.__ttl = ttl
        Element.__init__(self, position, velocity, angle)

    def get_size(self):
        return self.TORPEDO_SIZE

    def get_life_time(self):
        return self.__ttl

    def decrease_life_time(self):
        self.__ttl -= 1
