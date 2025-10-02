import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor('black')  # Set the background color to black

# Create a new turtle
heart = turtle.Turtle()
heart.speed(1)  # Set the speed of the drawing
heart.color('pink')  # Set the color to pink

def draw_heart(turtle):
    """
    Function to draw a heart shape with a given turtle.
    """
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-100, 200)
    turtle.left(120)
    turtle.circle(-100, 200)
    turtle.forward(180)

draw_heart(heart)

turtle.done()
