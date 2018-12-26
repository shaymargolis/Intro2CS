############################################################
# FILE : game.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex9 2018-2019
# DESCRIPTION : A class representing the game
#############################################################

import sys

from helper import load_json
from car import Car
from board import Board

LEGAL_NAMES = ["Y", "B", "O", "G", "W", "R"]
LEGAL_DIRECTIONS = ["u", "d", "l", "r"]


class Game:
    """
    Manages the rush hour game, reads the current
    board from car_config.json and places the cars.
    then asks for user input until the finish of
    the game.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """

        self.board = board

    def __single_turn(self):
        """
        Assks user to move a car and moves it,
        shows error on bad move or input or
        good on success.
        :return: returns True if victory is aquired,
        False otherwise.
        """

        result = input("Enter car and direction (Y,r): ")
        result = result.split(",")

        if len(result) != 2:
            return False

        move = self.board.move_car(result[0], result[1])

        if not move:
            print("The move is not legal!")
            return False

        print("Car moved successfuly.")
        #  Check if car was moved to the end

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """

        #  Until victory cell is not filled by the car
        while self.board.cell_content(self.board.target_location()) is not "R":
            #  Print current boad
            print(self.board)

            #  Ask for next move
            self.__single_turn()

        print("---- VICTORY! -----")
        print(self.board)
        print("VICTORY!")


def get_car_from_json(data):
    """
    Reads car object from json data,
    and returns it or none on bad data.
    :param data: Json array of Car
    :return: Car object or None
    """

    #  If the car color is not a valid one
    if name not in LEGAL_NAMES:
        return None

    #  Not valid array
    if len(data[name]) != 3:
        return None

    length = data[name][0]
    pos = data[name][1]
    orientation = data[name][2]

    return Car(name, length, pos, orientation)

if __name__ == "__main__":
    #  Get arguments from cmd
    args = sys.argv

    if len(args) != 2:
        print("Please add json file as a parameter.")
        exit(1)

    #  Create board
    board = Board()

    #  Load basic board information from file
    data = load_json(args[1])

    #  Load cars to board
    for name in data:
        car = get_car_from_json(data)
        board.add_car(car)

    #  create game object and start game
    game = Game(board)
    game.play()

