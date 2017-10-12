import turtle
 
myTurtle = turtle.Turtle()

def circles(velocity,size ):
    myTurtle.pencolor("red")
    myTurtle.speed(velocity)
    myTurtle.circle(size)
    
for i in range(566666666666): 
    circles(10,100)

#maximum speed of circle is 10    

#turtle.getscreen()._root.mainloop()
