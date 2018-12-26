############################################################
# FILE : board.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex9 2018-2019
# DESCRIPTION : A class representing the board
#############################################################

BOARD_LEN = 7  # Size of board
ORIENT_VERTICAL = 0
ORIENT_HORIZONTAL = 1


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        #  Generate the data array
        array = list()
        for i in range(BOARD_LEN):
            array.append([None for j in range(BOARD_LEN+1)])

        self.array = array
        self.cars = dict()

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """

        string = ""
        for i in range(BOARD_LEN):
            #  Create row and then print it
            row = ""
            for j in range(BOARD_LEN):
                val = self.cell_content((i, j))
                if val is None:
                    row += "_" + " "
                    continue

                row += str(self.array[i][j]) + " "

            if (i, j+1) == self.target_location():
                string += row + "E\n"
            else:
                string += row + "*\n"

        return string

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """

        result = list()

        for i in range(BOARD_LEN):
            for j in range(BOARD_LEN):
                result.append((i, j))

        result.append(self.target_location())

        return result

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """

        result = list()
        movekeys = ['l', 'r', 'u', 'd']

        for car_name in self.cars:
            car = self.cars[car_name]
            for movekey in movekeys:
                #  Check if movekey is okay
                if not car.move(movekey):
                    continue

                #  Check if requirement are met
                positions = car.movement_requirements(movekey)
                for pos in positions:
                    if self.cell_content(pos) is not None:
                        continue

                result.append((car.get_name(), movekeys, "Some description"))

        return result

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """

        return 3, 7

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """

        if tuple(coordinate) == self.target_location():
            return self.array[coordinate[0]][coordinate[1]]

        if coordinate[0] >= BOARD_LEN or coordinate[1] >= BOARD_LEN \
            or coordinate[0] < 0 or coordinate[1] < 0:
            return '*'

        return self.array[coordinate[0]][coordinate[1]]

    def update_cell(self, coordinate, value):
        """
        Updates a given coordinate
        :param coordinate: tuple of (row,col) of the coordinate to check
        :param value: New value
        :return: none
        """

        if coordinate[0] >= BOARD_LEN or coordinate[1] >= BOARD_LEN+1:
            return

        self.array[coordinate[0]][coordinate[1]] = value

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """

        #  Check if same name does not
        #  exists
        if self.cars.get(car.get_name()) is not None:
            return False

        coords = car.car_coordinates()
        for coord in coords:
            #  If the board in the wanted location
            #  is not empty, then it is occupied
            #  and the insert is illegal.
            if self.cell_content(coord) is not None:
                return False

        #  Add the car
        for coord in coords:
            self.update_cell(coord, car.get_name())

        #  Lastly, add the car to the dictionary
        self.cars[car.get_name()] = car

        return True

    def __remove_car(self, name):
        """
        Removes a car from the board.
        :param name: Name of car
        :return: True upon success, False otherwise
        """

        #  Check if car exists
        car = self.cars.get(name)
        if car is None:
            return False

        #  Delete every cell
        cords = car.car_coordinates()
        for cord in cords:
            self.update_cell(cord, None)

        self.cars.pop(name)

        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """

        car = self.cars.get(name)
        if car is None:
            return False

        #  Check if requirement are met
        positions = car.movement_requirements(movekey)
        for pos in positions:
            if self.cell_content(pos) is not None:
                return False

        if not self.__remove_car(name):
            return False

        #  Check if movekey is okay
        if not car.move(movekey):
            return False

        return self.add_car(car)
