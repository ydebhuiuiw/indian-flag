import turtle
from pygame import mixer
t=turtle.Turtle()
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()

t.pensize(3)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#ashok chakra
t.color('#050F88')
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)
move(0, -80)
t.circle(80, 360)

#green
t.begin_fill()
t.color("green")
t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()
#orange color
t.color("orange")
move(-350,80)
t.begin_fill()
t.right(180)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()
