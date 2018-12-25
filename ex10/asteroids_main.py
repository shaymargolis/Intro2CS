from screen import Screen
from ship import Ship
import sys
import random
import math

DEFAULT_ASTEROIDS_NUM = 5
TURNING_ANGLE = 7

class GameRunner:
    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        random_pos = self._random_position()
        velocity = (0, 0)
        self.__ship = Ship(random_pos, velocity, 0)

        self.__draw_ship()

    def __draw_ship(self):
        position = self.__ship.get_position()
        angle = self.__ship.get_angle()
        self.__screen.draw_ship(position[0], position[1], angle)

    def set_next_position(self):
        """
        Sets next position by current velocity, according
        to the time step dt.
        :param dt: time in [s]
        :return:
        """

        ship = self.__ship

        ship_velocity = ship.get_velocity()
        min_x, max_x, min_y, max_y = self.__screen_min_x, self.__screen_max_x, \
                                     self.__screen_min_y, self.__screen_max_y
        delta_x = max_x - min_x
        delta_y = max_y - min_y
        position_x = (ship.position[0] + ship_velocity[
            0] - min_x) % delta_x + min_x
        position_y = (ship.position[1] + ship_velocity[
            1] - min_y) % delta_y + min_y
        ship.set_position([position_x, position_y])

    def turn_ship(self, angle):
        self.__ship.set_angle(self.__ship.get_angle() + angle)

    def accelerate_ship(self):
        """ to do: change back acceleration"""
        ship_velocity = self.__ship.get_velocity()
        ship_angle = self.__ship.get_angle()
        velocity_x = ship_velocity[0] + 0.2 * math.cos(
            ship_angle * math.pi / 180)
        velocity_y = ship_velocity[1] + 0.2 * math.sin(
            ship_angle * math.pi / 180)

        self.__ship.set_velocity((velocity_x, velocity_y))

    def _random_position(self):
        """
        Returns random position between
        the boundries of the board
        :return:
        """
        random_x = random.uniform(
            self.__screen_min_x,
            self.__screen_max_x
        )
        random_y = random.uniform(
            self.__screen_min_y,
            self.__screen_max_y
        )

        return random_x, random_y

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        # Your code goes here
        ship_position = self.__ship.get_position()
        ship_velocity = self.__ship.get_velocity()
        ship_angle = self.__ship.get_angle()

        if self.__screen.is_left_pressed():
            #  Move angle of ship
            self.turn_ship(TURNING_ANGLE)

        if self.__screen.is_right_pressed():
            #  Move angle of ship
            self.turn_ship(TURNING_ANGLE)

        if self.__screen.is_up_pressed():
            #  Accelerate ship
            self.accelerate_ship()

        # Move ship by velocity
        self.set_next_position()

        #  Draw ship again
        self.__draw_ship()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
