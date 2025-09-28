import turtle

turtle.Screen().bgcolor("Green")
arrow = turtle.Turtle()
turtle.Screen().setup(500, 500)

arrow.forward(100)
arrow.left(120)

arrow.forward(100)
arrow.left(120)
arrow.forward(100)

arrow.penup()
arrow.right(150)
arrow.forward(70)

arrow.right(150)
arrow.pendown()
arrow.forward(100)
arrow.left(120)
arrow.forward(100)
arrow.left(120)
arrow.forward(100)
turtle.done()