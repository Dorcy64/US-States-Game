import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
score = 0
game_on = True
while game_on:
    ask = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()
    if ask in all_states:
        marker = turtle.Turtle()
        marker.penup()
        marker.hideturtle()
        marker.speed("fastest")
        new_cor = data[data["state"] == ask]
        new_x = int(new_cor["x"])
        new_y = int(new_cor["y"])
        marker.goto(new_x, new_y)
        marker.write(ask, align="center", move=False, font=("Arial", 12, "normal"))
        all_states.remove(ask)
        score += 1
    elif ask == "Exit":
        states_dict = {
            "States": all_states
        }
        to_write = pandas.DataFrame.from_dict(states_dict)
        to_write.to_csv("forgot_these.csv")
        game_on = False

screen.exitonclick()
