import turtle

silly =turtle.Turtle()
milly = turtle.Screen()
silly.shape('turtle')

def hexagon(x , y, length):
    silly.penup()
    silly.setpos(x, y)
    silly.pendown()
    for x in range (5):
       silly.forward(length)
       silly.left(90)
silly.color("blue")
for x in range(50):
    hexagon(x*2, x*3, x*2)
silly.color("red")
for x in range(50):
    hexagon(x*2, x*3, x*2)

milly.mainloop()

