#############################################################
# FILE : hello_turtle.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex1 2018-2019
# DESCRIPTION : A program that draws 3 flowers on a window
# using turtle.
#############################################################

import turtle


def draw_petal():
    """ Draws a single petal using turtle """
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100,90)


def draw_flower():
    """ draws a single flower using turtle """
    # draws the top-right petal
    turtle.setheading(0)
    draw_petal()
    # draws the top-left petal
    turtle.setheading(90)
    draw_petal()
    # draws the bottom-left petal
    turtle.setheading(180)
    draw_petal()
    # draws the bottom-right petal
    turtle.setheading(270)
    draw_petal()
    # draws the line beneath the flower
    turtle.setheading(270)
    turtle.forward(250)


def draw_flower_advance():
    """ draws a single flower and places the turtle
        in point for next flower draw """
    draw_flower()
    # moves the turtle without drawing to the same height,
    # but more to the left, where we started drawing the
    # last flower.
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """ draws 3 flowers from the right to the left
        in the middle of the window """
    # moves the turtle without drawing to the left,
    # so the flowers will be centered
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    # draws 3 flowers from the right to the left
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()

if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done()