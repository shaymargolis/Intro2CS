import utills as ut
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import sys
import random
import math


DEFAULT_ASTEROIDS_NUM = 5
TURNING_ANGLE = 7
U_SPD_LIM = 4
L_SPD_LIM = 1
ASTEROID_SIZE = 3
HIT_TITLE = "OH NO!"
HIT_MESSAGE = "It seems like you were hit and lost a life! watch out!"
SHIP_LIFE = 3

SHOULD_END_MESSAGE = "You asked for quit. Hope to see you again!"
WIN_MESSAGE = "Yay! You won!"
LOOSE_MESSAGE = "Oh no! you just died."
LOOSE_TITLE = "you LOST!"
WIN_TITLE = "you WON!"


class GameRunner:
    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        velocity = (0, 0)

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        random_pos = self._random_position()
        self.__ship = Ship(random_pos, velocity, 0,SHIP_LIFE)
        self.__draw_ship()

        self.__torpedos = []

        self.__asteroids = []
        for i in range(asteroids_amount):
            random_pos = self._random_position()
            while ut.distance(random_pos, self.__ship.get_position()) <= 3:
                random_pos = self._random_position()
            random_vel = ut.random_speed()
            asteroid = Asteroid(random_pos, random_vel, ASTEROID_SIZE)
            self.__screen.register_asteroid(asteroid, ASTEROID_SIZE)
            self.__asteroids.append(asteroid)

    def __draw_ship(self):
        position = self.__ship.get_position()
        angle = self.__ship.get_angle()
        self.__screen.draw_ship(position[0], position[1], angle)

    def set_next_position(self, elem):
        """
        Sets next position by current velocity, according
        to the time step dt.
        :param dt: time in [s]
        :return:
        """

        ship_velocity = elem.get_velocity()
        min_x, max_x, min_y, max_y = self.__screen_min_x, self.__screen_max_x, \
                                     self.__screen_min_y, self.__screen_max_y
        delta_x = max_x - min_x
        delta_y = max_y - min_y
        position_x = (elem.position[0] + ship_velocity[
            0] - min_x) % delta_x + min_x
        position_y = (elem.position[1] + ship_velocity[
            1] - min_y) % delta_y + min_y
        elem.set_position([position_x, position_y])

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

    def launch_torpedo(self):
        #  Get launch parameters from current
        #  position and angle of the ship
        position = self.__ship.get_position()
        velocity = self.__ship.get_velocity()
        angle = self.__ship.get_angle()

        #  Calculate velocity in both axis
        #  accordingly
        v_x = velocity[0] + 2 * math.cos(
            angle * math.pi / 180
        )

        v_y = velocity[1] + 2 * math.sin(
            angle * math.pi / 180
        )

        #  Add torpedo to draw list
        torpedo = Torpedo(position, [v_x, v_y], angle)
        self.__torpedos.append(torpedo)

        #  Make screen aware of torpedo
        self.__screen.register_torpedo(torpedo)

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

        #  Check for teleport
        if self.__screen.is_teleport_pressed():
            #  Get a random position
            #  That is atleast 3 distances
            #  away from any asteroid.
            position = self._random_position()
            min_distance = 0
            while min_distance <= 3:
                random_pos = self._random_position()
                #  Get the minimal distance from
                #  the asteroids.
                min_distance = min(map(
                    lambda x: ut.distance(random_pos, x.get_position()),
                    self.__asteroids
                ))

            #  Set the position
            self.__ship.set_position(position)

        if self.__screen.is_left_pressed():
            #  Move angle of ship
            self.turn_ship(TURNING_ANGLE)

        if self.__screen.is_right_pressed():
            #  Move angle of ship
            self.turn_ship(-TURNING_ANGLE)

        if self.__screen.is_up_pressed():
            #  Accelerate ship
            self.accelerate_ship()

        if self.__screen.is_space_pressed():
            #  Create torpedo
            self.launch_torpedo()

        # Move ship by velocity
        self.set_next_position(self.__ship)

        # Move torpedos by velocity
        for torpedo in self.__torpedos:
            self.set_next_position(torpedo)
            position = torpedo.position
            angle = torpedo.angle
            self.__screen.draw_torpedo(torpedo, position[0], position[1],
                                       angle)

        for ast in self.__asteroids:
            if ast.has_intersection(self.__ship):
                self.__ship.decrease_life()
                self.__screen.remove_life()
                self.__screen.show_message(HIT_TITLE, HIT_MESSAGE)
                self.__asteroids.remove(ast)
                self.__screen.unregister_asteroid(ast)
            else:
                self.set_next_position(ast)
                position = ast.position
                self.__screen.draw_asteroid(ast, position[0], position[1])


        # Draw ship again
        self.__draw_ship()

        #  Check for victory
        #  The user pressed 'q'
        end = False

        if self.__screen.should_end():
            self.__screen.show_message(SHOULD_END_MESSAGE)
            end = True

        if len(self.__asteroids) == 0:
            self.__screen.show_message(WIN_TITLE,WIN_MESSAGE)
            end = True

        if self.__ship.get_life() == 0:
            self.__screen.show_message(LOOSE_TITLE,LOOSE_MESSAGE)
            end = True

        if end:
            self.__screen.end_game()
            sys.exit(0)


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
