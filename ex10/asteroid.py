############################################################
# FILE : asteroid.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the asteroid
#############################################################

from element import Element
import utills as u


class Asteroid(Element):
    """
    Asteroid element that contains functions
    for determining the properties of the
    asteroid.
    """

    SIZE_FACTOR = 10
    NORMAL_FACTOR = 5

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
        """
        Returns the size of the asteroid
        :return:
        """
        return self.size

    def set_size(self, new_size):
        """
        Sets the size of the asteroid
        :param new_size:
        :return:
        """
        self.size = new_size

    def get_radius(self):
        """
        Returns the radius of the asteroids
        :return:
        """
        return self.get_size() * self.SIZE_FACTOR - self.NORMAL_FACTOR

    def has_intersection(self, obj):
        """
        Checks if the asteroid (self) has an intersection
        with obj element.
        :param obj: An element
        :return:
        """
        d = u.distance(self.get_position(), obj.get_position())
        return d <= self.get_radius() + obj.get_radius()

    def get_score(self):
        """
        Returns the score that will be given
        if a torpedo hits the asteroid according
        to the size
        :return: The score
        """

        if self.size == 1:
            return 100

        if self.size == 2:
            return 50

        return 20
