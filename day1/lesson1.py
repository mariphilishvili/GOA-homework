from turtle import *


#i want to paint a house

#step 1: drawing a square
width(7)
color("pink")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square



#drawing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("cyan")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 150)  
pendown()

color("red")
begin_fill()
right(60)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

#drawing windows

penup()
goto(180, 150)  
pendown()
left(90)
color("red")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

end_fill()


exitonclick()