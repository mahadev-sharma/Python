import turtle

silly = turtle.Turtle()
silly.pencolor("red")
def square(size = 100 ,angle = 110):
    
    silly.forward(size)
    silly.right(angle)     # Rotate clockwise by 90 degrees
    
    silly.forward(size)
    silly.right(angle)
    
    silly.forward(size)
    silly.right(angle)
    
    silly.forward(size)
    silly.right(100)
    
for i in range(103):
     square()
     
silly.pencolor("black")

for i in range(103):
     square()
