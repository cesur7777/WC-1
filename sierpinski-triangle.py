import turtle

kose_uzunlugu = 600

s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor("white")
t.pencolor("red")
t.speed(0)

t.penup()
t.goto(-400,-300)
t.pendown()
t.begin_fill()
for i in range(3):
    t.forward(kose_uzunlugu)
    t.left(120)

def sierpinski(uzunluk, derinlik):
    if derinlik == 0:
        return
    else:
        t.begin_fill()
        for i in range(3):
            t.forward(uzunluk/2)
            sierpinski(uzunluk/2, derinlik-1)
            t.forward(uzunluk/2)
            t.left(120)
        t.end_fill()

t.penup
t.goto(-400,-300)
t.pendown()
sierpinski(kose_uzunlugu , 4)

turtle.done()
