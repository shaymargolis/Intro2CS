############################################################
# FILE : asteroid.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the asteroid
#############################################################

from element import Element


class Asteroid(Element):

    def __init__(self, position, velocity, size):
        """
        Creates a asteroid instance
        :param position: A position vector (x,y)
        :param velocity: A velocity vector (V_x, V_y)
        :param size: The size of the asteroid from 1 to 3
        :return:
        """

        Element.__init__(self, position, velocity, 0)
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, new_size):
        self.size = new_size