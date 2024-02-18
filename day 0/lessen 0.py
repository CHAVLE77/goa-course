from turtle import *


#we want to paint a house
speed(30)
#step:1 draw a square
width(7)
color("purple")
begin_fill()
forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
end_fill()


#end of square

#drawing a door
forward (70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of door

penup()
goto(200,200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

#drawing a window
color("yellow")
begin_fill()
left(30)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()
#end window

color("purple")
right(90)
forward(140)
color("yellow")
begin_fill()
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

exitonclick()