from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clean_screen():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)  # without ()
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clean_screen)

screen.exitonclick()