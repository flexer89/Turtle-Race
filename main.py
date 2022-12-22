import random
import turtle

x = 1024
y = 768
is_race_on = False

screen = turtle.Screen()
screen.setup(x, y)
screen.title("Turtle race")

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
turtle_list = []
bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

if bet:
    is_race_on = True

#Turtle creating
for turtle_index in range(6):
    tim = turtle.Turtle(shape="turtle")
    tim.turtlesize(2)
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-x/2+30, y_positions[turtle_index])
    tim.setheading(0)
    turtle_list.append(tim)

#Game flow
while is_race_on:
    for turtle in turtle_list:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 1024/2:
            is_race_on = False
            winner_color = turtle.pencolor()
            if bet == winner_color:
                print("You Win!")
            print(f"You lose. The winner is {winner_color}")

screen.exitonclick()
