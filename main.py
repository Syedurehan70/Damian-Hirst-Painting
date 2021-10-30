import turtle as t
import random
# we got this list from extraction code
color_list = [(243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31),
              (219, 129, 166), (161, 79, 35), (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42),
              (180, 45, 94), (30, 136, 81), (236, 164, 193), (78, 12, 63), (12, 54, 33), (234, 227, 7), (26, 165, 209),
              (16, 43, 132), (58, 166, 96), (134, 214, 229), (10, 101, 63), (133, 34, 20), (91, 27, 11),
              (159, 211, 188)]

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setposition(-200.00, -200.00)
tim.pendown()


def vertical():
    for i in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

a = 50.00
for i in range(10):
    vertical()
    tim.setposition(-200.00, -200.00 + a)
    a += 50.00


screen = t.Screen()
screen.exitonclick()