############################################################
# FILE : car.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex9 2018-2019
# DESCRIPTION : A class representing the cars
#############################################################

import board as b
import numpy as np


class Car:
    """
    Add class description here
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """

        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def get_step(self, movekey):
        """
        Returns move step according to the movekey
        :param movekey: directions tr
        :return: move vector
        """
        step = [0, 0]

        if movekey == 'r':
            step = (0, 1)
        if movekey == 'l':
            step = (0, -1)
        if movekey == 'u':
            step = (-1, 0)
        if movekey == 'd':
            step = (1, 0)

        return step

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """

        #  Get move step from orientation
        movekey = 'd'
        if self.orientation == b.ORIENT_HORIZONTAL:
            movekey = 'r'
        step = self.get_step(movekey)

        #  Calculate all coordinates of car
        result = list()
        for i in range(self.length):
            new = tuple(np.add(self.location, np.multiply(step, i)))
            result.append(new)

        return result

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """

        if self.orientation == b.ORIENT_VERTICAL:
            return {
                'u': "Moves the car up",
                'd': "Moves the car down"
            }

        return {
            'r': "Moves the car right",
            'l': "Moves the car left"
        }

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """

        step = self.get_step(movekey)
        if sum(step) > 0:
            start = tuple(np.add(self.location, np.multiply(step, self.length-1)))
        else:
            start = self.location

        return [tuple(np.add(start, step))]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """

        if self.orientation == b.ORIENT_HORIZONTAL \
            and movekey not in ['r', 'l']:
            return False

        if self.orientation == b.ORIENT_VERTICAL \
            and movekey not in ['d', 'u']:
            return False

        self.location = tuple(np.add(self.location, self.get_step(movekey)))

        return True

    def get_name(self):
        """
        :return: The name of this car.
        """

        return self.name
