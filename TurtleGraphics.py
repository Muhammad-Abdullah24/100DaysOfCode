import random
from turtle import *
from HirstProject import colors


my_turtle = Turtle()
screen = Screen()
colormode(255)
not_done = True
i = 0

my_turtle.up()

my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

while not_done:
    my_turtle.dot(10,colors[random.randint(0, len(colors) - 1)])
    my_turtle.up()
    my_turtle.forward(50)

    i += 1
    if i % 10 == 0:  
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

    my_turtle.down()

    if i >= 100:
        not_done = False

screen.exitonclick()


