############################################################
# FILE : element.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the element
#############################################################


class Element:

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
        return self.position

    def get_velocity(self):
        return self.velocity

    def get_angle(self):
        return self.angle

    def set_position(self, new_position):
        self.position = new_position

    def set_velocity(self, new_velocity):
        self.velocity = new_velocity

    def set_angle(self, new_angle):
        self.angle = new_angle