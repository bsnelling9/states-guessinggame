import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer = screen.textinput(title=f"{len(guess_states)}/50 Guess the State",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        states_learn = [state for state in states if state not in guess_states]
        df = pandas.DataFrame(states_learn)
        df.to_csv("states_to_learn.csv")

        break

    if answer in states:
        guess_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)





