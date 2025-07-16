from turtle import Turtle, Screen
import random

color_list = ["red", "blue", "green", "yellow", "purple", "orange",
              "pink", "brown", "cyan", "magenta","black"]
y_values = [-30, 10, 50, 90]

def create_turtle(x, y):
    turtle = Turtle()
    color = random.choice(color_list)
    color_list.remove(color)
    turtle.color(color)
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x,y)
    return turtle

def move_turtle(turtle):
    distance = random.randint(0, 10)
    turtle.forward(distance)

screen = Screen()
screen.setup(width=600, height=400)
turtles = []
user_bet = screen.textinput("CHOOSE YOUR TURTLE","What color turtle will win?")

x = -250
turtle = Turtle()
turtle.color(user_bet)
color_list.remove(user_bet)
turtle.shape("turtle")
turtle.penup()
turtle.goto(x,-70)
turtles.append(turtle)

for i in range(0, 4):
    y = 0
    turtles.append(create_turtle(x, y_values[i]))

flag = True

while flag:
    for turtle in turtles:
        move_turtle(turtle)
        if turtle.xcor() >= 275:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput("RESULT", f"You've won! The {winning_color} turtle is the winner!")
                flag = False
                break
            else:
                screen.textinput("RESULT", f"You've lost! The {winning_color} turtle is the winner!")
                flag = False
                break
screen.exitonclick()