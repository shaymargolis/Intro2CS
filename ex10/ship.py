############################################################
# FILE : ship.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the ship
#############################################################

from element import Element


class Ship(Element):

    def __init__(self, position, velocity, angle):
        """
        Creates a ship class instance
        :param position: position vector (x,y)
        :param velocity: velocity vector (v_x, v_y)
        :param angle: angle in degrees
        :return:
        """

        Element.__init__(self, position, velocity, angle)

    def set_next_position(self, dt):
        """
        Sets next position by current velocity, according
        to the time step dt.
        :param dt: time in [s]
        :return:
        """

        ship_velocity = self.get_velocity()
        position_x = self.position[0] + ship_velocity[0] * dt
        position_y = self.position[1] + ship_velocity[1] * dt

        self.set_position((position_x, position_y))
