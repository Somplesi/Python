########### Challenge 2 - Draw a Dashed Line ########
# https://docs.python.org/3/library/turtle.html
import turtle as t

tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()