__author__ = 'T8698819'
from asteroids_main import *
import math


def random_speed():
    """
    Returns random speeds between
    the boundries of the speed
    :return:
    """
    random_x = random.uniform(
        L_SPD_LIM,
        U_SPD_LIM
    )
    random_y = random.uniform(
        L_SPD_LIM,
        U_SPD_LIM
    )

    return random_x, random_y


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[2]) ** 2)
