from turtle import*

def main():
	speed("fastest")
	background()
	pu()
	home()
	pd()
	speed("normal")
	head()
	shell()
	feet()
	tail()

	done()

def background():

	size=0
	pensize(6)

	for i in range (350):
		if i%2==0:
			colour = "red"
		else:
			colour = "blue"
		color(colour)
		forward(size)
		right(91)
		size+=4

def head():

	pu()
	#goto(150,50)
	pd()
	#pen(fillcolor="green", pencolor="black", pensize=5)
	begin_fill()
	right(90)
	#circle(100,-200)
	#left(100)
	#fd(50)
	right(180)
	#fd(35)
	right(145)
	#fd(110)
	right(30)
	#fd(70)
	#goto(150,50)
	end_full()

	eye()

def eye():

	right(165)
	pu()
	fd(150)
	pd()

	circle(10)

def shell():

	pu()
	goto(150,50)
	#pen(fillcolor="saddlebrown", pencolor="black", pensize=5)
	pd()
	begin_fill()
	left(95)
	circle(250,170)
	left(86)
	fd(510)
	goto(150,50)
	end_fill()
	shell_arrangement()

def shell_arrangement():
	pu()
	goto(-300,30)
	pd()
	for i in range (8):
		if i < 3:
			shell_pattern()
			pu()
			right(136)
			fd(110)
			pd()
		elif i==3:
			shell_pattern()
			pu()
			right(25)
			fd(90)
			right(90)
			pd()
		elif i==4:
			shell_pattern()
			pu()
			right(6)
			fd(120)
			right(120)
			pd()
		elif i==5:
			shell_pattern()
			pu()
			left(30)
			fd(60)
			pd()
		elif i==6:
			shell_pattern()
			pu()
			fd(40)
			pd()
		else:
			shell_pattern()


def shell_pattern():

	left(40)
	fd(50)
	right(45)
	fd(40)
	right(70)
	fd(40)
	right(70)
	fd(40)
	right(40)
	fd(30)
	right(38)
	fd(38)

def feet():
	#pen(fillcolor="green", pencolor="black", pensize=5)
	pu()
	goto(-250,-20)
	right(207)
	pd()
	feet2()

	right(90)
	pu()
	fd(380)
	right(90)
	pd()
	feet2()

	pu()
	right(90)
	fd(120)
	right(90)
	fd(18)
	right(360)
	pd()
	feet1()

	pu()
	right(180)
	fd(280)
	right(270)
	pd()
	feet1()

def feet1():
	begin_fill()
	for i in range (3):
		fd(50)
		right(90)
	end_fill()

def feet2():
	begin_fill()
	fd(80)
	right(90)
	fd(50)
	right(90)
	fd(80)
	end_fill()

def tail():

	pu()
	goto(-340,20)
	right(210)
	pd()
	begin_fill()
	fd(40)
	right(150)
	fd(40)
	end_fill()
	ht()


main()
