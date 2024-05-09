import pandas
from turtle import Screen, Turtle, shape

screen = Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state


class StateWriter(Turtle):
    def __init__(self, data):
        super().__init__(visible=False)
        self.penup()
        self.data = data

    def write_state(self, state_item):
        row = self.data[self.data.state == state_item]
        x = int(row.x)
        y = int(row.y)
        self.goto(x, y)
        self.write(state_item, align="center", font=("Ariel", 10, "normal"))

    def win(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Ariel", 10, "normal"))


jenny = StateWriter(data)
guessed_states = []

while len(guessed_states) != 50:
    answer_state = screen.textinput(f"Guess the state. {len(guessed_states)}/50",
                                    prompt="What's another states name?").title()
    if answer_state == "Exit":
        data_list = [state for state in states.to_list() if state not in guessed_states]
        pandas.DataFrame(data_list).to_csv("missing_states.csv")
        break
    if answer_state in states.to_list():
        guessed_states.append(answer_state)
        jenny.write_state(answer_state)

screen.exitonclick()
