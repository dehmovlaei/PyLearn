import turtle
import math

colors = ["blue","red"]
r = 15
n = 3
x = 0

p = turtle.Pen()
p.shape("turtle")
p.width(3)

while True:
    for j in range(len(colors)):
        p.pencolor(colors[j])
        for i in range(n):
            if i == 0:
                p.left((360-((n-2)*180/n))/2)
                
            else:
                p.left(360/n)    
            p.forward(2*r*math.sin(math.pi/n))
        r += 10
        n += 1
        x += 10
        p.penup()
        p.goto(x, 0)
        p.pendown()
        p.setheading(0)
