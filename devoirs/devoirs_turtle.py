import turtle

screen = turtle.Screen()
screen.mainloop()
point = turtle.Turtle()
point.penup()
point.shape("circle")
point.color("red")
point.goto(100, 100) 
def verifier_arrivee():
    point.hideturtle() #permet de cacher le cercle rouge