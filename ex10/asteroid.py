############################################################
# FILE : asteroid.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the asteroid
#############################################################


class Asteroid:

    def __init__(self, position, velocity, size):
        """
        Creates a asteroid instance
        :param position: A position vector (x,y)
        :param velocity: A velocity vector (V_x, V_y)
        :param size: The size of the asteroid from 1 to 3
        :return:
        """

        self.position = position
        self.velocity = velocity
        self.size = size


