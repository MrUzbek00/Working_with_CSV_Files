from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("U.S. States Games")
turtle = Turtle()
image = "D:/Python/100 days Python Challenge/Intermediate/day 25/blank_states_img.gif"
file_path = "D:/Python/100 days Python Challenge/Intermediate/day 25/50_states.csv"
screen.addshape(image)
turtle.shape(image)
file =pandas.read_csv(file_path)
# Gets the the tauched place`s coordinates
# def get_mouse_click_coor(x, y):
#     turtle.onscreenclick(None)
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
guessed_state =[]
state_list = file.state.to_list()
learn_states =[]
while len(guessed_state) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_state)}/50 Guess the state", 
                                   prompt="What`s another state`s name?").title()
    
    if user_answer == "Exit":
        break
    if user_answer in state_list:
        guessed_state.append(user_answer)
        coor = file[file.state == user_answer]
        coor_x = int(coor.x.item())  # Convert to int
        coor_y = int(coor.y.item())
    
        name = Turtle()
        # name.hideturtle()
        name.shape("circle")
        name.resizemode(rmode="user")
        name.shapesize(stretch_wid=0.3, stretch_len=0.3)
        name.color("red")
        name.penup()
        name.goto(coor_x, coor_y)
        name.write(user_answer, move=False, font=("Arial", 8, "normal"))

for state in state_list:
    if state not in guessed_state:
        learn_states.append(state) 

new_df = pandas.DataFrame(learn_states)

new_df.to_csv("Need to repeat.csv")



        





