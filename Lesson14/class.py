import turtle 
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()
num_side = 6
side_len = 80
angle = 360/num_side
for i in range(num_side):
    polygon.forward(side_len)
    polygon.right(angle)

turtle.done()
