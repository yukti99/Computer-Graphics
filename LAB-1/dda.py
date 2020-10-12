from graphics import *


def dda(p0,p1):	
	win = GraphWin("My Line using DDA", 900, 700)	
	dx = p1[0] - p0[0]
	dy = p1[1] - p0[1]
	if (abs(dx) > abs(dy)):
		steps = abs(dx)
	else:
		steps = abs(dy)
	xi = dx/float(steps)
	yi = dy/float(steps)
	x = p0[0]
	y = p0[1]
	print(steps)
	for i in range(0,steps+1):
			
		point = Point(x,y)
		point.draw(win)
		x += xi
		y += yi
	win.getMouse()	
	win.close()		
		

def main():
	p0 = (50,60)
	p1 = (788,239)			
	dda(p0,p1)
	

main()
