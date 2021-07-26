# Import modules:
import turtle
import pandas
import states
import text_on_screen

# Open a csv file:
data = pandas.read_csv('50_states.csv')
data_list = data["state"].to_list()

# Setup the message turtle:
message = text_on_screen.Message()

# Setup the state turtle:
state = states.State()

# Setup the screen:
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgpic('blank_states_img.gif')

# Main loop:
list_of_answers = []
score = 0
keep_going = True
while keep_going:
    # Ask user:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state?")
    answer_title = answer.title()

    # Check if user answer was right:
    cors = data[data["state"] == answer_title]

    message.clear()  # Clearing the screen from any messages

    # Exit the game and save data into csv:


    if answer_title in data_list:
        # Check if answer not repeats.
        if answer_title in list_of_answers:
            message.repeated()

        # Write the state on the screen and store it in the list.
        state.goto(float(cors["x"]), float(cors["y"]))
        state.write(answer_title, False, align="center", font=("Comic Sans", 10, "normal"))
        list_of_answers.append(answer_title)
        score += 1

    # If answer is wrong
    elif answer_title not in list_of_answers:
        message.wrong()

    # Ending the game:
    if score >= 51:
        keep_going = False

# Exit on click:
screen.exitonclick()
