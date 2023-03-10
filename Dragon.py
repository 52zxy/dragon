import turtle
t = turtle.Turtle()
s = turtle.Screen()

#head
t.color("black", "pink")
t.begin_fill()
t.circle(80)
t.end_fill()

#eyes
t.penup()
t.left(90)
t.forward(85)
t.right(90)
t.forward(30)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()
t.backward(60)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(15)
t.end_fill()

#face
t.penup()
t.right(90)
t.forward(45)
t.left(90)
t.pendown()
t.forward(60)

#body
t.penup()
t.backward(30)
t.right(90)
t.forward(40)
t.pendown()
t.color("black", "#FDEFB2")
t.begin_fill()
t.forward(175)
t.right(90)
t.forward(400)
t.right(90)
t.forward(175)
t.right(90)
t.forward(400)
t.end_fill()

#legs
t.penup()
t.backward(300)
t.right(90)
t.forward(175)
t.pendown()
t.color("black", "#FDEFB2")
t.begin_fill()
t.forward(45)
t.right(90)
t.forward(35)
t.right(90)
t.forward(45)
t.right(90)
t.forward(35)
t.end_fill()

t.penup()
t.backward(45)
t.right(90)
t.pendown()
t.color("black", "#FDEFB2")
t.begin_fill()
t.forward(45)
t.right(90)
t.forward(35)
t.right(90)
t.forward(45)
t.right(90)
t.forward(35)
t.end_fill()

#wings
t.penup()
t.forward(250)
t.left(90)
t.forward(135)
t.left(35)
t.pendown()
t.color("black", "pink")
t.begin_fill()
t.forward(250)
t.left(125)
t.forward(100)
t.left(55)
t.forward(135.28)
t.left(55)
t.forward(100)
t.end_fill()

#tail
t.penup()
t.backward(305)
t.right(180)
t.pendown()
t.color("black", "pink")
t.begin_fill()
t.forward(100)
t.left(150)
t.forward(115)
t.left(120)
t.forward(58)
t.end_fill()

#tail spikes
spikes = 0
t.left(90)
t.color("black", "#FDEFB2")
t.begin_fill()
while spikes < 4:
    t.right(45)
    t.forward(18)
    t.left(90)
    t.forward(18)
    t.right(45)
    spikes = spikes + 1
t.backward(100)
t.end_fill()

s.exitonclick()