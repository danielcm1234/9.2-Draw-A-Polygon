from turtle import *

def regular_polygon(t, sides, length):
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

def draw_square(t):
    t.penup()
    t.goto(-75, -75)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(150)
        t.left(90)
    t.end_fill()

def draw_rectangle(t):
    t.penup()
    t.goto(-100, -60)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(120)
        t.left(90)
    t.end_fill()

def draw_parallelogram(t):
    t.penup()
    t.goto(-100, -60)
    t.pendown()
    t.begin_fill()
    t.forward(180)
    t.left(60)
    t.forward(120)
    t.left(120)
    t.forward(180)
    t.left(60)
    t.forward(120)
    t.end_fill()

def draw_trapezoid(t):
    t.penup()
    t.goto(-100, -60)
    t.pendown()
    t.begin_fill()
    t.forward(200)
    t.left(120)
    t.forward(80)
    t.left(60)
    t.forward(120)
    t.left(60)
    t.forward(80)
    t.end_fill()

def draw_unknown_quadrilateral(t):
    t.penup()
    t.goto(-80, 60)
    t.pendown()
    t.begin_fill()
    t.goto(40, 90)
    t.goto(100, -30)
    t.goto(-20, -100)
    t.goto(-100, -20)
    t.goto(-80, 60)
    t.end_fill()

window = Screen()
window.bgcolor("black")
window.title("Polygons")
window.setup(width=800, height=800)

pen = Turtle()
pen.color("white")
pen.shape("turtle")
pen.penup()
pen.pensize(5)
pen.hideturtle()
pen.speed(0)
while True:
    sides = int(input("How many sides? "))

    pen.clear()

    if sides < 3:
        print("Polygons need at least 3 sides.")
    elif sides == 3:
        print("Triangle")
        pen.pendown()
        pen.penup()
        pen.goto(-60, -40)
        pen.pendown()
        regular_polygon(pen, 3, 160)
    elif sides == 4:
        parallel_pairs = int(input("How many parallel pairs? (0, 1, 2) "))

        if parallel_pairs == 0:
            print("Unknown quadrilateral")
            draw_unknown_quadrilateral(pen)
        elif parallel_pairs == 1:
            print("Trapezoid")
            draw_trapezoid(pen)
        else:
            same_sides = input("Are all sides the same length? (yes/no) ").lower()

            if same_sides == "yes":
                print("Square")
                draw_square(pen)
            else:
                same_angles = input("Do all angles have the same measurement? (yes/no) ").lower()

                if same_angles == "yes":
                    print("Rectangle")
                    draw_rectangle(pen)
                else:
                    print("Parallelogram")
                    draw_parallelogram(pen)

    elif sides == 5:
        print("Pentagon")
        pen.penup()
        pen.goto(-60, -40)
        pen.pendown()
        regular_polygon(pen, 5, 120)
    elif sides == 6:
        print("Hexagon")
        pen.penup()
        pen.goto(-60, -20)
        pen.pendown()
        regular_polygon(pen, 6, 100)
    else:
        print("Unknown")
        pen.penup()
        pen.goto(-60, -20)
        pen.pendown()
        regular_polygon(pen, sides, 100)

window.mainloop()
