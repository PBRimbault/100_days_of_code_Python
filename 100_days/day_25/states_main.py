import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True

data = pandas.read_csv("50_states.csv")

score = 0

guessed_states = []

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        states_to_learn = [check_state for check_state in data.state if check_state not in guessed_states]
        data = pandas.DataFrame(states_to_learn)
        data.to_csv("states_to_learn.csv")
        break

    for state in data.state:
        if score < 50:  
            if answer_state == state:
                score += 1
                state_name = turtle.Turtle()
                state_name.hideturtle()
                state_name.penup()
                state_x = int(data[data.state == state].x)
                state_y = int(data[data.state == state].y)
                state_name.goto(state_x, state_y)
                state_name.write(state, align="center")
                guessed_states.append(answer_state)



        

# screen.exitonclick()