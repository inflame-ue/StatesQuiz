# TODO: Create a USA states quiz.

# Import modules:
import turtle
import pandas
import constants

# Open a csv file:
data = pandas.read_csv('50_states.csv', sep=",", encoding="utf8")
data_dict = data.to_dict()

# Setup the screen:
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgpic('blank_states_img.gif')

# Ask user:
answer = screen.textinput(title="Guess the State", prompt="What's another state?")
answer_title = answer.title()

# Check if user answer was right:
if answer_title in data_dict:







# Exit on click:
screen.exitonclick()
