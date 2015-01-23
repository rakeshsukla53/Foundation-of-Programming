__author__ = 'rsukla'

import turtle
import time

window = turtle.Screen()
window.bgcolor("Red")

def draw_square(brad):

    for i in range(0, 4):
        brad.forward(100)
        brad.right(90)

def draw_circle():

    brad = turtle.Turtle()
    for i in range(0, 50):
        draw_square(brad)
        brad.right(10)


draw_circle()

