import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
df = pandas.read_csv("50_states.csv")
states_list = df['state'].to_list()
game_on = True
correct_states = 0
answered_states = []
my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()

while len(answered_states) < len(states_list):
    if answer_state == "Exit":
        print('a')
        missing_states = []
        for state in states_list:
            if state not in answered_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('missing_states.csv')
        break
    elif answer_state in states_list and answer_state not in answered_states:
        x_cor = int(df[df['state'] == answer_state]['x'])
        y_cor = int(df[df['state'] == answer_state]['y'])
        correct_states += 1
        my_turtle.goto(x_cor, y_cor)
        my_turtle.write(answer_state)
        answered_states.append(answer_state)
    answer_state = screen.textinput(title=f"{len(answered_states)}/50 Correct Sates", prompt="What's another state's name?").title()

screen.exitonclick()
