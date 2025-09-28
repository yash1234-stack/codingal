import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(500, 500)
arr = turtle.Turtle()
spiralsize = 0

while(spiralsize!=200):
    arr.forward(spiralsize)
    arr.right(90)
    spiralsize = spiralsize+5


turtle.done()