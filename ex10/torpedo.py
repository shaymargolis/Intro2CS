############################################################
# FILE : torpedo.py
# WRITER : shay margolis , roy amir
# EXERCISE : intro2cs1 ex10 2018-2019
# DESCRIPTION : A class representing the torpedo
#############################################################


class Torpedo:

    def __init__(self, position, velocity, angle):
        """
        Creates a torpedo class instance
        :param position: position vector (x,y)
        :param velocity: velocity vector (v_x, v_y)
        :param angle: angle in degrees
        :return:
        """

        self.position = position
        self.velocity = velocity
        self.angle = angle