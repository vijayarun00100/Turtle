from turtle import *

CURSOR_SIZE = 20

radius, height = [50, 200]  # in pixels

shape('square')
shapesize(radius*2 / CURSOR_SIZE, height / CURSOR_SIZE)
fillcolor('white')
stamp()

shape('circle')
shapesize(stretch_len=radius / CURSOR_SIZE)
backward(height/2)
stamp()

forward(5)
pencolor('white')
stamp()

forward(height - 5)
color('black')
stamp()

done()
