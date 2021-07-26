# Import turtle
import turtle


# Create a new message class:
class Message(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.speed(0)

    def repeated(self):
        self.clear()
        self.color("coral")
        self.write("You already guessed this state.", False, align="center", font=("Comic Sans", 20, "normal"))

    def right_answer(self):
        self.clear()
        self.color("green")
        self.write("Oh! You guessed it all right!", False, align="center", font=("Comic Sans", 20, "normal"))

    def wrong(self):
        self.clear()
        self.color("red")
        self.write("It's wrong!", False, align="center", font=("Comic Sans", 20, "normal"))
