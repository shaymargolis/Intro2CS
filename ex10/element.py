############################################################
# FILE : element.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the element
#############################################################


class Element:
    """
    Contains general variables that are
    shared between the different elements
    in the program that is used to detrmine
    the position and next position in the screen.
    """

    def __init__(self, position, velocity, angle):
        """
        Creates a element instance
        :param position: A position vector [x,y]
        :param velocity: A velocity vector [V_x, V_y]
        :param size: The size of the asteroid from 1 to 3
        :return:
        """

        self.position = position
        self.velocity = velocity
        self.angle = angle

    def get_position(self):
        """
        Returns the position of the element
        :return: Position as 2d array
        """
        return self.position

    def get_velocity(self):
        """
        Returns the velocity of the element.
        :return: Velocity as [x,y] array
        """
        return self.velocity

    def get_angle(self):
        """
        Returns the angle of the element.
        :return: Angle in degrees
        """
        return self.angle

    def set_position(self, new_position):
        """
        Sets the position of the element
        :param new_position: New position array
        of 2 axis
        :return:
        """
        self.position = new_position

    def set_velocity(self, new_velocity):
        """
        Sets the velocity of the element.
        :param new_velocity: new velocity array
        of 2 axis
        :return:
        """
        self.velocity = new_velocity

    def set_angle(self, new_angle):
        """
        Set the angle of the element
        :param new_angle: New angle in degrees
        :return:
        """
        self.angle = new_angle