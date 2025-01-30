import turtle
t=turtle.Turtle()
screen = turtle.Screen()
point = turtle.Turtle()
point.penup()
point.shape("circle")
point.color("red")
point.goto(100, 100)  # Position du point rouge
def up () :
    t.setheading(90)
    t.forward(20)
def down():
    t.setheading(270)
    t.forward(20)
def left():
    t.setheading(180)
    t.forward(20)
def right():
    t.setheading(0)
    t.forward(20)
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.mainloop()