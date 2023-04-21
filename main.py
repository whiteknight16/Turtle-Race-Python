from turtle import Turtle,Screen
from random import randint

isRaceOn=False

screen=Screen()
screen.setup(width=500,height=400)

colors=["black","blue","green","yellow","orange","red"]
turtle_list=[]

z=-100
for i in range (len(colors)):
    t1=Turtle(shape="turtle")
    t1.color(colors[i])
    t1.pu()
    t1.goto(x=-240,y=z+50*i)
    turtle_list.append(t1)

user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ").lower()

if (user_bet):
    isRaceOn=True

while(isRaceOn):
    for turtle in turtle_list:
        random_distance=randint(0,10)
        turtle.fd(random_distance)
        if (turtle.xcor()>=220):
            winner_color=turtle.pencolor()
            isRaceOn=False
if (winner_color==user_bet):
    print(f"Congrats !! {user_bet} won 🥳")
else:
    print(f"Alas!! {user_bet} lost 😔 , {winner_color} won")





screen.exitonclick()