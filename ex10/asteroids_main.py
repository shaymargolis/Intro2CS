import utills as ut
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
from special import Special
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
INIT_SCORE = 0

SHOULD_END_TITLE = "Quitting"
SHOULD_END_MESSAGE = "You asked for quit. Hope to see you again!"
WIN_MESSAGE = "Yay! You won!"
LOOSE_MESSAGE = "Oh no! you just died."
LOOSE_TITLE = "you LOST!"
WIN_TITLE = "you WON!"
TORPEDO_LIMIT = 10
SPECIAL_LIMIT = 5
SPECIAL_FACTOR = 10

class GameRunner:
    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        velocity = (0, 0)

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        self.__score = INIT_SCORE

        random_pos = self._random_position()
        self.__ship = Ship(random_pos, velocity, 0, SHIP_LIFE)
        self.__draw_ship()

        self.__torpedos = []
        self.__specials = []

        self.__init_asteroid(asteroids_amount)

    def __init_asteroid(self, asteroids_amount):
        """
        Adds the initial asteroids according to
        the starting asteroids_amount
        :param asteroids_amount: The amount to add
        :return:
        """

        #  Create new asteroids array
        self.__asteroids = []

        for i in range(asteroids_amount):
            #  Create an random position that
            #  is far enough from the ship
            random_pos = self._random_position()
            while ut.distance(random_pos, self.__ship.get_position()) <= 3:
                random_pos = self._random_position()

            # Get a random speed
            random_vel = ut.random_speed()

            #  Add the asteroid to the system
            asteroid = Asteroid(random_pos, random_vel, ASTEROID_SIZE)
            self.__screen.register_asteroid(asteroid, ASTEROID_SIZE)
            self.__asteroids.append(asteroid)

    def __draw_ship(self):
        """
        Draws the current position of the speed
        to the screen
        :return:
        """
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

        #  Calculate next position according to the velocity
        #  according to the formula
        position_x = \
            (elem.position[0] + ship_velocity[0] - min_x) % delta_x \
            + min_x
        position_y = \
            (elem.position[1] + ship_velocity[1] - min_y) % delta_y \
            + min_y

        elem.set_position([position_x, position_y])

    def turn_ship(self, angle):
        """
        Turns the ship by a specific angle
        (degrees)
        :param angle: The angle to move by.
        :return:
        """
        self.__ship.set_angle(self.__ship.get_angle() + angle)

    def accelerate_ship(self):
        """
        Accelerates ship (After up press)
        :return:
        """

        #  Get current velocity and angle
        ship_velocity = self.__ship.get_velocity()
        ship_angle = self.__ship.get_angle()

        #  Calculate velocity by formula
        velocity_x = ship_velocity[0] + math.cos(
            ship_angle * math.pi / 180)
        velocity_y = ship_velocity[1] + math.sin(
            ship_angle * math.pi / 180)

        self.__ship.set_velocity((velocity_x, velocity_y))

    def launch_special(self):
        """
        Launches special shot from current position
        of the space ship.
        :return:
        """
        #  Get launch parameters from current
        #  position and angle of the ship
        position = self.__ship.get_position()
        for i in range(5):
            special = Special(position, [SPECIAL_FACTOR*math.sin((i*360/5)/360*2*math.pi), SPECIAL_FACTOR*math.cos((i*360/5)/360*2*math.pi)], i*360/5)
            self.__specials.append(special)
            self.__screen.register_torpedo(special)

    def launch_torpedo(self):
        """
        Launches torpedo from current position
        of the space ship.
        :return:
        """
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

    def split_asteroid(self, asteroid, torpedo):
        """
        Removes asteroid from the screen and splits
        it if the size is more than 1.
        :param asteroid: the asteroid to split
        :param torpedo: the torpedo that hit
        :return:
        """

        #  Remove the asteroid from the screen
        size = asteroid.get_size() - 1
        self.__asteroids.remove(asteroid)
        self.__screen.unregister_asteroid(asteroid)

        #  Only if size-1 of the asteroid is not 0,
        #  split the asteroid to 2.
        if size > 0:
            position = asteroid.get_position()
            v_asteroid = asteroid.get_velocity()
            v_torpedo = torpedo.get_velocity()

            #  Calculate new speed by the formula
            v_norm = math.sqrt(
                v_asteroid[0] ** 2 + v_asteroid[1] ** 2
            )

            v_x = (v_asteroid[0] + v_torpedo[0]) / v_norm
            v_y = (v_asteroid[1] + v_torpedo[1]) / v_norm

            #  Add 2 asteroid with reversed velocities
            asteroid1 = Asteroid(position, [v_x, v_y], size)
            asteroid2 = Asteroid(position, [-v_x, -v_y], size)

            self.__screen.register_asteroid(asteroid1, size)
            self.__asteroids.append(asteroid1)
            self.__screen.register_asteroid(asteroid2, size)
            self.__asteroids.append(asteroid2)

    def intersect_torpedo_asteroid(self, asteroid, torpedo):
        """
        Runs the code that intersect torpedo and asteroid,
        and splits the asteroid
        :param asteroid: The asteroid to split
        :param torpedo: The torpedo that hits the asteroid
        :return: NOTHING
        """

        #  Increment the score, set it and
        #  remove the torpedo
        self.__score += asteroid.get_score()
        self.__screen.set_score(self.__score)
        self.__screen.unregister_torpedo(torpedo)
        if isinstance(torpedo,Special):
            self.__specials.remove(torpedo)
        elif isinstance(torpedo,Torpedo):
            self.__torpedos.remove(torpedo)

        #  Split the asteroid
        self.split_asteroid(asteroid, torpedo)

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

    def teleport(self):
        """
        Teleports the ship to a location that
        is not occupied by a asteroid
        :return:
        """
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

        # Set the position
        self.__ship.set_position(position)

    def check_for_end(self):
        """
        Checks if the end of the game came,
        by different methods of game ending.
        :return:
        """
        #  Flag to know if we should
        #  exit the game window
        end = False

        #  The user pressed 'q'
        if self.__screen.should_end():
            self.__screen.show_message(SHOULD_END_TITLE, SHOULD_END_MESSAGE)
            end = True

        # There are no asteroids left
        if len(self.__asteroids) == 0:
            self.__screen.show_message(WIN_TITLE, WIN_MESSAGE)
            end = True

        # The user is out of life
        if self.__ship.get_life() == 0:
            self.__screen.show_message(LOOSE_TITLE, LOOSE_MESSAGE)
            end = True

        if end:
            self.__screen.end_game()
            sys.exit(0)

    def update_torpedoes(self):
        """
        Moves the torpedoes to the next
        location according to their speed.
        Checks if every torpedo has hit an
        asteroid and split it accordingly
        :return:
        """
        objects = self.__torpedos+self.__specials
        for torpedo in objects:
            #  If the torpedo is out of life,
            #  remove it.
            if torpedo.get_life_time() <= 0:
                self.__screen.unregister_torpedo(torpedo)
                if isinstance(torpedo, Special):
                    self.__specials.remove(torpedo)
                elif isinstance(torpedo, Torpedo):
                    self.__torpedos.remove(torpedo)
                continue

            # Move the torpedo to next location
            self.set_next_position(torpedo)
            position = torpedo.position
            angle = torpedo.angle
            self.__screen.draw_torpedo(torpedo, position[0], position[1],
                                       angle)
            torpedo.decrease_life_time()

            #  Check if the torpedo hit an asteroid
            intersection = torpedo.has_intersection(self.__asteroids)

            if intersection is not None:
                self.intersect_torpedo_asteroid(intersection, torpedo)

    def update_asteroids(self):
        """
        Moves the asteroids to the next
        location according to their speed,
        decreases life of ship if hits a ship.
        :return:
        """
        for ast in self.__asteroids:
            #  Move asteroid to next position
            self.set_next_position(ast)
            position = ast.position
            self.__screen.draw_asteroid(ast, position[0], position[1])

            #  Check if we hit a ship, and if yes
            #  remove the asteroids, decrease life
            #  and show message
            if ast.has_intersection(self.__ship):
                self.__ship.decrease_life()
                self.__screen.remove_life()
                self.__screen.show_message(HIT_TITLE, HIT_MESSAGE)
                self.__asteroids.remove(ast)
                self.__screen.unregister_asteroid(ast)

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
        """
        The main game loop.
        :return:
        """
        #  Check for key presses
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
            if len(self.__torpedos) < TORPEDO_LIMIT:
                self.launch_torpedo()

        if self.__screen.is_special_pressed():
            # create special
            if len(self.__specials) < SPECIAL_LIMIT:
                self.launch_special()

        # Move ship by velocity
        self.set_next_position(self.__ship)

        # Move torpedos by velocity
        self.update_torpedoes()
        self.update_asteroids()

        # Draw ship again
        self.__draw_ship()

        #  Check for end of game
        self.check_for_end()

        #  Check for teleport
        if self.__screen.is_teleport_pressed():
            self.teleport()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
