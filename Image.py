import turtle as t
t.setup(width=800, height=600)
t.shape("turtle")
t.speed(25)
t.color("Tan")
t.begin_fill()
t.penup()
t.goto(-650,-335)
t.pendown()
for i in range(2):
    t.forward(1450)
    t.left(90)
    t.forward(250)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-650,-85)
t.pendown()
t.color("light blue")
t.begin_fill()
for i in range(2):
    t.forward(1450)
    t.left(90)
    t.forward(515)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-45,-85)
t.pendown()
t.color("blue")
t.begin_fill()
for i in range(2):
    t.forward(200)
    t.left(120)
t.forward(100)
t.end_fill()
t.left(120)
t.penup()
t.goto(90,-85)
t.pendown()
t.color("dark orange")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.left(120)
t.forward(300)
t.end_fill()
t.left(120)
t.penup()
t.goto(325,-85)
t.pendown()
t.color("purple")
t.begin_fill()
for i in range(2):
    t.forward(150)
    t.left(120)
t.forward(150)
t.end_fill()
t.left(120)
t.left(90)
t.speed(13)
t.penup()
t.goto(-450,-200)
t.pendown()
t.color("brown")
t.begin_fill()
t.forward(50)
t.end_fill()
t.right(90)
t.color("green")
t.begin_fill()
t.circle(25)
t.end_fill()
t.left(90)
t.penup()
t.goto(-375,-275)
t.pendown()
t.color("brown")
t.begin_fill()
t.forward(50)
t.end_fill()
t.right(90)
t.color("green")
t.begin_fill()
t.circle(25)
t.end_fill()
t.left(90)
t.penup()
t.goto(-295,-200)
t.pendown()
t.color("brown")
t.begin_fill()
t.forward(50)
t.end_fill()
t.right(90)
t.color("green")
t.begin_fill()
t.circle(25)
t.end_fill()
t.left(90)
t.penup()
t.goto(-215,-275)
t.pendown()
t.color("brown")
t.begin_fill()
t.forward(50)
t.end_fill()
t.right(90)
t.color("green")
t.begin_fill()
t.circle(25)
t.end_fill()
t.left(90)
t.penup()
t.goto(-525,-275)
t.pendown()
t.color("brown")
t.begin_fill()
t.forward(50)
t.end_fill()
t.right(90)
t.color("green")
t.begin_fill()
t.circle(25)
t.end_fill()
t.penup()
t.goto(-115,225)
t.pendown()
t.speed(15)
t.pencolor("black")
for i in range(2):
    t.right(120)
    t.forward(25)
t.right(120)
t.penup()
t.goto(-200,205)
t.pendown()
for i in range(2):
    t.right(120)
    t.forward(25)
t.right(120)
t.penup()
t.goto(-275,240)
t.pendown()
for i in range(2):
    t.right(120)
    t.forward(25)
t.color("gray")
t.begin_fill()
t.penup()
t.goto(150,275)
t.pendown()
t.circle(25)
t.end_fill()
t.begin_fill()
t.penup()
t.goto(180,278)
t.pendown()
t.circle(25)
t.end_fill()
t.begin_fill()
t.penup()
t.goto(200,275)
t.pendown()
t.circle(25)
t.end_fill()
t.penup()
t.goto(-530,275)
t.pendown()
t.color('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(-505,175)
t.pendown()
t.forward(25)
t.penup()
t.goto(-530,130)
t.pendown()
t.forward(25)
t.penup()
t.goto(-555,90)
t.pendown()
t.forward(25)
t.penup()
t.goto(-485,60)
t.pendown()
t.forward(25)
t.penup()
t.goto(-510,5)
t.pendown()
t.forward(25)
t.penup()
t.goto(-455,-25)
t.pendown()
t.forward(25)
t.penup()
t.goto(-390,-60)
t.pendown()
t.forward(25)
t.penup()
t.goto(335,290)
t.pendown()
t.pencolor("black")
t.left(60)
t.forward(45)
t.left(140)
t.forward(45)
t.right(140)
t.forward(45)
t.penup()
t.goto(345,290)
t.pendown()
t.left(120)
t.forward(35)
t.left(120)
t.forward(35)
t.left(30)
t.penup()
t.goto(395,255)
t.pendown()
t.color("black")
t.forward(35)
t.penup()
t.goto(405,305)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(455,275)
t.pendown()
t.circle(20)
t.right(90)
t.penup()
t.goto(450,260)
t.pendown()
t.forward(15)
t.right(90)
t.penup()
t.goto(485,305)
t.pendown()
t.forward(45)
t.left(90)
t.forward(20)
t.penup()
t.goto(475,280)
t.pendown()
t.forward(30)
t.penup()
t.goto(150,150)
t.pendown()
t.done()

# import turtle
# import colorsys
# t = turtle.Turtle()
# s= turtle.Screen().bgcolor("black")
# t.speed(0)
# n = 70
# h = 0
# for i in range (360):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h+= 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for i in range (2):
#         t.left(2)
#         t.circle(100)
