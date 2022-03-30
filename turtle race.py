from turtle import Turtle, Screen
import random

isRaceOn = False
screen = Screen()
screen.title('Turtle Racing Game')
screen.setup(width=500, height=400)
userGuess = screen.textinput(title="Guess", prompt="who will win? Enter a color: ")
colors = ['red','orange','yellow','green','blue','purple']
y_pos = [-70, -40, -10, 20, 50, 80]
allTurtle = []

for turtleIndex in range(0,6):
  tim = Turtle(shape="turtle")
  tim.color(colors[turtleIndex])
  tim.penup()
  tim.goto(x=-230, y=y_pos[turtleIndex])
  allTurtle.append(tim)
  
if userGuess:
  isRaceOn = True

while isRaceOn:

  for turtle in allTurtle:
    if turtle.xcor() > 230:
      isRaceOn = False
      win = turtle.pencolor()
      if win == userGuess:
        print('WOW!!! You won...')
      else:
        print('Opps!!! You lost...')
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)

screen.exitonclick()
