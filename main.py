import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Whitch turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "cyan"]
all_turtles = []

# how many turtles in a race?
n_turtles = screen.textinput(title="How many turtles", prompt="How many turtles in a race? (max 11) : ")
no = int(n_turtles)

y_line = -150
for turtle_new in range(0, no):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_new])
    new_turtle.goto(x=-230, y=y_line)
    y_line += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
