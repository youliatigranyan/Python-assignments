import turtle
turtle.Screen().bgcolor("lightgreen")

#------------------------------hexagon----------------------------

y = turtle.Turtle()
y.speed(5)
y.color("hotpink")
def triangle(edge=100):
    y.forward(edge)
    y.right(120)
    y.forward(edge)
    y.right(120)
    y.forward(edge)
    y.right(180)

for _ in range(6):
    triangle()

y.penup()
y.hideturtle()


#------------------------------minnie----------------------------

minnie = turtle.Turtle()

def minniex():
    minnie.speed(5)
    minnie.shape("turtle")
    minnie.color("hotpink")
    minnie.penup()

    minnie.forward(200)
    minnie.left(90)

    minnie.pendown()
    minnie.backward(50)

    minnie.begin_fill()
    minnie.fillcolor('hotpink')
    for _ in range(5):

        minnie.forward(100)
        minnie.right(90)
    minnie.end_fill()


    minnie.pendown()
    minnie.begin_fill()
    minnie.fillcolor('hotpink')
    minnie.circle(30)
    minnie.end_fill()

    minnie.begin_fill()
    minnie.fillcolor('black')
    minnie.circle(20)
    minnie.end_fill()

    minnie.penup()
    minnie.forward(100)

    minnie.pendown()
    minnie.begin_fill()
    minnie.fillcolor('hotpink')
    minnie.circle(30)
    minnie.end_fill()

    minnie.begin_fill()
    minnie.fillcolor('black')
    minnie.circle(20)
    minnie.end_fill()

    minnie.penup()
    minnie.right(90)
    minnie.forward(20)
    minnie.right(90)
    minnie.forward(20)

    minnie.begin_fill()
    minnie.fillcolor('black')
    minnie.pendown()
    minnie.circle(12)
    minnie.end_fill()

    minnie.penup()
    minnie.forward(60)

    minnie.begin_fill()
    minnie.fillcolor('black')
    minnie.pendown()
    minnie.circle(12)
    minnie.end_fill()

    minnie.penup()
    minnie.backward(30)
    minnie.left(90)
    minnie.forward(20)

    minnie.begin_fill()
    minnie.fillcolor('black')
    minnie.pendown()
    minnie.left(30)
    minnie.forward(20)
    minnie.right(120)
    minnie.forward(20)
    minnie.right(120)
    minnie.forward(20)
    minnie.right(150)
    minnie.end_fill()

    minnie.penup()
    minnie.forward(30)
    minnie.right(90)
    minnie.forward(20)
    minnie.left(90)

    minnie.begin_fill()
    minnie.fillcolor('black')
    minnie.pendown()
    minnie.circle(20,180)
    minnie.end_fill()

minniex()
minnie.hideturtle()


#------------------------------applelogo----------------------------
apple = turtle.Turtle()

def applelogo():
    apple.begin_fill()
    apple.fillcolor('hotpink')
    apple.speed(10)
    apple.shape("arrow")

    apple.penup()
    apple.backward(180)
    apple.pendown()

    apple.left(134)

    for i in range(30):
        apple.forward(1)
        apple.left(1)

    apple.right(5)

    for i in range(35):
        apple.forward(1)
        apple.left(1)

    apple.left(5)
    apple.forward(30)

    for i in range(15):
        apple.forward(0.7)
        apple.right(3)

    apple.forward(25)
    apple.left(5)

    for i in range(50):
        apple.forward(1)
        apple.left(1)

    apple.right(3)

    for i in range(50):
        apple.forward(1)
        apple.left(1)

    apple.right(5)

    for i in range(45):
        apple.forward(2)
        apple.left(1)

    apple.right(5)

    for i in range(40):
        apple.forward(2)
        apple.left(1)

    apple.left(5)

    for i in range(20):
        apple.forward(1)
        apple.left(2)

    apple.left(5)
    apple.forward(15)

    for i in range(9):
        apple.forward(2)
        apple.right(3)

    apple.forward(1)

    for i in range(15):
        apple.forward(1)
        apple.right(1)

    apple.right(4)
    apple.forward(4.5)
    apple.right(1)

    for i in range(27):
        apple.forward(1)
        apple.left(2)

    apple.left(8)
    apple.forward(5)

    for i in range(25):
        apple.forward(2)
        apple.left(1)

    apple.right(3)
    apple.forward(10)
    apple.left(83)

    for i in range(75):
        apple.forward(1.3)
        apple.right(1)

    apple.right(4)

    for i in range(24):
        apple.forward(1.3)
        apple.right(1)

    apple.forward(9.66)

    apple.penup()

    apple.left(132)
    apple.forward(100)
    apple.right(96)

    apple.pendown()


    for i in range(60):
        apple.forward(1.5)
        apple.right(1)

    apple.right(120)

    for i in range(60):
        apple.forward(1.5)
        apple.right(1)

    apple.end_fill()

applelogo()
