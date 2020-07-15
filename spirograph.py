
"""
Created on Wed Jul 15 17:26:03 2020

@author: Sivaraman Sivaraj
"""


import turtle

turtle.bgcolor("green")
turtle.pensize(2)
turtle.speed(12)


colors = ['red','magenta', 'blue', 'cyan','green', 'yellow', 'white']

for i in range(6):
    for clr in colors:
        turtle.color(clr)
        turtle.circle(100)
        turtle.left(10)
        
turtle.hideturtle()
turtle.bye()
