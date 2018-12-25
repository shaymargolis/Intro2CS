############################################################
# FILE : torpedo.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the torpedo
#############################################################

from element import Element
import utills as uti

TORPEDO_SIZE = 4


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

    def get_radius (self):
        return TORPEDO_SIZE

    def has_intersection(self, list):
        """
        Checks if torpedo has an intersection
        with one of the elements in list, if
        yes it returns the first element in it.
        :param list: List of elemenets
        :return: Element it is going to intersect with
        or none
        """

        for elem in list:
            d = uti.distance(self.get_position(), elem.get_position())
            if d <= self.get_radius() + elem.get_radius():
                return elem

        return None
