from turtle import *
from random import randint
#Add the following code to draw a line using the ‘turtle’
#forward(100)

#The turtle write function writes text to the screen.
#write(0)
#forward(20)
speed(10)
penup()
goto(-140,140)
for step in range(15):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
tur = Turtle()
tur.color('red')
tur.shape('turtle')

tur.penup()
tur.goto(-160,100)
tur.pendown()

mark = Turtle()
mark.color('blue')
mark.shape('turtle')
mark.penup()
mark.goto(-160,70)
mark.pendown()

john = Turtle()
john.color('green')
john.shape('turtle')
john.penup()
john.goto(-160,40)
john.pendown()


joj = Turtle()
joj.color('yellow')
joj.shape('turtle')
joj.penup()
joj.goto(-160,10)
joj.pendown()

for turn in range(100):
    tur.forward(randint(1,5))
    mark.forward(randint(1,5))
    john.forward(randint(1,5))
    joj.forward(randint(1,5))
