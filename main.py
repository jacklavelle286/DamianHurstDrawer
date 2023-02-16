import turtle
from turtle import Turtle, Screen
import random
from random import randint
color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176),
              (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50),
              (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86),
              (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161),
              (152, 213, 190), (242, 205, 8), (89, 48, 31), (39, 46, 81), (26, 97, 94)]

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.speed("fastest")
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

turtle.penup()


def move_forward():
    for _ in range(9):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)


def turn_left():
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)


def turn_right():
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


for lines in range(5):
    move_forward()
    turn_left()
    move_forward()
    turn_right()

