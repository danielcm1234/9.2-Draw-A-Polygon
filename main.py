from turtle import *

def regular_polygon(turtle,sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(200/sides)
        turtle.left(360/sides)
    turtle.end_fill()

window = Screen()
window.bgcolor("black")
window.title("Polygons")
window.setup(width = 800, height = 800)

turtle = Turtle()
turtle.color("white")
turtle.shape("turtle")
turtle.penup()
turtle.pensize(5)
turtle.hideturtle()
turtle.speed(0)

while True:
    sides = int(input("how many sides do you want?"))
    turtle.clear()
    if int(sides) < 3:
        pen.write("polygons must have at least 3 sides.")
    elif sides!= 4:
        regular_polygon(turtle, sides)




window.exitonclick()