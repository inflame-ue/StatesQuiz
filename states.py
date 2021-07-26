# Import modules:
import turtle


# Create a new state class:
class State(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.speed(0)
        self.color("black")
