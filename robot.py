'''
Directions:
Working with a partner, draw a robot with random-sized arms, legs, head, and hat.
You should define separate functions for arms, legs, head, and hat.
Split up the work so that each partner defines two functions.
When finished, combine your code.
'''
from turtle import *
from random import *

# create variables here
torsoWidth = randint(70,180)
torsoHeight = randint(70,180)
red = randint(0,255)
green = randint(0,255)
blue = randint(0,255)

# change the drawing settings here
tracer(1)
colormode(255)
color(red, green, blue)
fillcolor(255-red, 255-green, 255-blue)
pensize(5)

def rectangle(width,height):
    # use the given width and height
    for i in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)

def drawTorso():
    # move to the top-left corner
    penup()
    goto(0 - torsoWidth / 2, torsoHeight / 2)
    # draw the torso
    pendown()
    begin_fill()
    rectangle(torsoWidth, torsoHeight)
    end_fill()





drawTorso()
# draw arms
# draw legs
# draw head
# draw hat
update()