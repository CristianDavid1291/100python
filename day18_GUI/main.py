from turtle import Turtle, Screen
import random

basic_colors = ["red", "orange", "yellow", "green", "blue", "purple",
                 "pink", "brown", "black"]



def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def draw_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

def draw_shape(num_sides):
    tim.color(random.choice(basic_colors))
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_walk():
    tim.speed("fastest")
    tim.pensize(10)
    directions = [0, 90, 180, 270]
    for _ in range(200):
        tim.pencolor(generate_random_color())
        tim.setheading(random.choice(directions))
        tim.forward(20)


screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.penup()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)

def draw_circle_line():
    for _ in range(10):
        tim.speed("fastest")
        tim.dot(20, generate_random_color())
        tim.penup()
        if _ < 9:  
            tim.forward(40)
        tim.pendown()

# Optimized code to draw multiple lines of dots in a grid pattern

num_rows = 10
for row in range(num_rows):
    draw_circle_line()
    if row < num_rows - 1:
        tim.setheading(90)
        tim.penup()
        tim.forward(40)
        tim.setheading(180 if row % 2 == 0 else 0)
        
        


screen.exitonclick()