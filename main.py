from turtle import *

def regular_polygon(turtle,sides):
    turtle.beginfil()
    for i in sides:
        turtle.forward(200/sides)
        turtle.left(360,sides)
    turtle.end_fill()

window = Screen()
window.bgcolor("black")
window.title("Polygons")
window.setup(width = 800, height = 800)

while true:
    sides = input("how many sides do you want?")
    pen.clear()
    if sides < 3:
        pen.write("polygons must have at least 3 sides.")
    elif sides!= 4:
        regular_polygon(pen, sides)



window.exitonclick()