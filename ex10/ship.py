############################################################
# FILE : ship.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the ship
#############################################################

from element import Element


class Ship(Element):
    """
    Ship element that contains function
    for special properties of Ship.
    """

    SHIP_RADIUS = 1

    def __init__(self, position, velocity, angle,life):
        """
        Creates a ship class instance
        :param position: position vector (x,y)
        :param velocity: velocity vector (v_x, v_y)
        :param angle: angle in degrees
        :return:
        """
        self.__life = life
        Element.__init__(self, position, velocity, angle)

    def decrease_life(self):
        """
        Decreases life of ship by 1
        :return:
        """
        self.__life -= 1

    def get_life(self):
        """
        Returns total life of ship
        :return:
        """
        return self.__life

    def get_radius(self):
        """
        Returns radius of ship
        :return:
        """
        return self.SHIP_RADIUS
