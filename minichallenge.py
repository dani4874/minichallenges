import turtle
from turtle import *

try:
    input_file=open("maze.txt","r")
except IOError:
    print("cannot open", arg)
else:
    turtle=turtle.Turtle()
    counter=1
    x=0
    y=0
    xadd=0
    yadd=0
    for line in input_file:
        new=line.split(",")
        if counter%2!=0:
            for elements in new:
                if elements=="1":
                    turtle.goto((x+xadd),(y+yadd))
                    turtle.pendown()
                    forward(40)
                    turtle.penup()
                    xadd=xadd+40
                elif elements=="0":
                    turtle.penup()
                    position=position+40
                counter=counter+1
            yadd=yadd+40
        
finally:
    if input_file is not None:
        input_file.close()
