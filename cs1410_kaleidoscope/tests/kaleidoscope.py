"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import random


def get_player1():
    p1 = turtle.Turtle()
    p1.color("red")
    p1.shape("circle")
    p1.setheading(0)
    p1.pensize(5)
    return p1


def get_player2():
    p2 = turtle.Turtle()
    p2.color("blue")
    p2.shape("circle")
    p2.setheading(72)
    p2.pensize(5)
    return p2


def get_player3():
    p3 = turtle.Turtle()
    p3.color("green")
    p3.shape("circle")
    p3.setheading(144)
    p3.pensize(5)
    return p3


def get_player4():
    p4 = turtle.Turtle()
    p4.color("yellow")
    p4.shape("circle")
    p4.setheading(216)
    p4.pensize(5)
    return p4


def get_player5():
    p5 = turtle.Turtle()
    p5.color("purple")
    p5.shape("circle")
    p5.setheading(288)
    p5.pensize(5)
    return p5


def turn_right(p1, p2, p3, p4, p5):
    angle = random.randrange(180)
    p1.right(angle)
    p2.right(angle)
    p3.right(angle)
    p4.right(angle)
    p5.right(angle)


def turn_left(p1, p2, p3, p4, p5):
    angle = random.randrange(180)
    p1.left(angle)
    p2.left(angle)
    p3.left(angle)
    p4.left(angle)
    p5.left(angle)


def move(p1, p2, p3, p4, p5):
    dist = random.randrange(-50, 50)
    p1.forward(dist)
    p2.forward(dist)
    p3.forward(dist)
    p4.forward(dist)
    p5.forward(dist)


def random_stamp(p1, p2, p3, p4, p5):
    shapes = ["circle", "turtle", "square", "triangle", "classic"]
    myShape = shapes[random.randrange(len(shapes))]
    p1.shape(myShape)
    p2.shape(myShape)
    p3.shape(myShape)
    p4.shape(myShape)
    p5.shape(myShape)
    p1.stamp()
    p2.stamp()
    p3.stamp()
    p4.stamp()
    p5.stamp()
    p1.shape("circle")
    p2.shape("circle")
    p3.shape("circle")
    p4.shape("circle")
    p5.shape("circle")


def main():
    p1 = get_player1()
    p2 = get_player2()
    p3 = get_player3()
    p4 = get_player4()
    p5 = get_player5()
    num = random.randrange(15, 25)
    for i in range(num):
        move(p1, p2, p3, p4, p5)
        x = random.randrange(2)
        if x == 1:
            turn_right(p1, p2, p3, p4, p5)
        else:
            turn_left(p1, p2, p3, p4, p5)
        random_stamp(p1, p2, p3, p4, p5)


main()
