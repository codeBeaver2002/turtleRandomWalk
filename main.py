from turtle import *
from random import *
from time import *

colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


path = [0, 1, 2, 3]


def random_walk(tim):
    dist = 20
    randChoice = choice(path)
    if randChoice == 0:
        tim.forward(dist)
    elif randChoice == 1:
        tim.back(dist)
    elif randChoice == 2:
        tim.right(90)
        tim.forward(dist)
    else:
        tim.left(90)
        tim.forward(dist)


tim = Turtle()
tim.shape("triangle")
tim.pensize(5)
tim.speed(0)
count = 0


count = Turtle()
count.shape("circle")

count.speed(200)
count.penup()
count.goto(-400,350)
count3=0






for i in range(0,900):
    tim.color(random_color())
    count3 = 0 + i
    count.clear()
    count.write(count3, align="center", font=("arial", 24, "normal"))
    # sleep(1)
    random_walk(tim)



my_screen = Screen()
my_screen.exitonclick()