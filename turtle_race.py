import random
import turtle

is_race_on = False
screen = turtle.Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color")
print(user_bet)
colors = ["orange","red","blue","green","purple","yellow"]
y_postion = [-100,-60,-20,20,60,100]
all_turtle = []

for num in range(0,6):
    tim = turtle.Turtle(shape="turtle")
    tim.color(colors[num])
    tim.penup()
    tim.goto(-230,y_postion[num])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("You've won!")
            else:
                print("You've lose.")
        distance = random.randint(1,10)
        turtle.forward(distance)

screen.exitonclick()
