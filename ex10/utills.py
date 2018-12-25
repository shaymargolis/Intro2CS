__author__ = 'T8698819'

import asteroids_main as a
import random
import math


def random_speed():
    """
    Returns random speeds between
    the boundries of the speed
    :return:
    """
    random_x = random.uniform(
        a.L_SPD_LIM,
        a.U_SPD_LIM
    )
    random_y = random.uniform(
        a.L_SPD_LIM,
        a.U_SPD_LIM
    )

    return random_x, random_y


def distance(p1, p2):
    """
    returns the distance between p1 and p2
    :param p1: [x,y] array
    :param p2: [x,y] array
    :return: distance number
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
