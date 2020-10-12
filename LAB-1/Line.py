# Asssignment 1 - LINE by YUKTI KHURANA 2017UCP1234

from graphics import *

xwmin = 0
xwmax = 0
xvmin = 0
xvmax = 0
ywmin = 0
ywmax = 0
yvmin = 0
yvmax = 0


def transformX(xw):
	t = (xvmax-xvmin)/(xwmax-xwmin)
	xv = xvmin + ((xw-xwmin)*t)
	return int(xv)
	
def transformY(yw):
	t = (yvmax-yvmin)/(ywmax-ywmin)
	yv = yvmin + ((yw-ywmin)*t)
	return int(yv)

def bresenham(x0,y0,x1,y1,win):
	#transforming end points of the line
	x0 = transformX(x0)
	y0 = transformY(y0)
	x1 = transformX(x1)
	y1 = transformY(y1)	
	print("The viewport coordinates of point1 : ","(",x0,",",y0,")")
	print("The viewport coordinates of point2 : ","(",x1,",",y1,")")	
	#writing points
	pt1 = Point(x0,y0)
	pt1.setFill('purple')
	pt1.draw(win)
	p1 = Text(Point(x0,y0), "(%d,%d)"%(x0,y0))
	p1.setTextColor("green")
	p1.draw(win)	
	pt2 = Point(x1,y1)
	pt2.setFill('purple')
	pt2.draw(win)
	p2 = Text(Point(x1,y1), "(%d,%d)"%(x1,y1))
	p2.setTextColor("green")
	p2.draw(win)	
	dx = x1 - x0
	dy = y1 - y0
	xsign,ysign = 1,1	
	if (dx < 0):
		xsign=-1
	if(dy < 0):
		ysign=-1
	dx = abs(dx)
	dy = abs(dy)
	# if the slope of line < 1 
	if (dx > dy):
		xx=xsign
		xy=0
		yx=0
		yy=ysign
	else:
		#swapping the values of dy and dx for D initial
		dx,dy=dy,dx
		xx=0
		xy=ysign
		yx=xsign
		yy=0
	# Decision variable
	D = 2*dy - dx
	y = 0
	for x in range(dx + 1):
		a = x0 + x*xx + y*yx
		b = y0 + x*xy + y*yy
		#p = Point(transformX(a),transformY(b))
		p = Point(a,b)
		p.draw(win)
		p.setFill('purple')		
		# to show the simulation of line in an animated manner
		time.sleep(0.003)	
		if (D >= 0):
			y += 1
			D -= 2*dx
		D += 2*dy		
			

def main():
	global xwmin,xwmax,xvmin,xvmax,ywmin,ywmax,yvmin,yvmax	
	xvmin = -450
	yvmin = -450
	xvmax = 450	
	yvmax = 450
	xwmin = -2000
	ywmin = -2000
	xwmax = 2000	
	ywmax = 2000		
	print("Enter the end points of line:")
	x0 = int(input("Enter x0 = "))
	y0 = int(input("Enter y0 = "))
	x1 = int(input("Enter x1 = "))
	y1 = int(input("Enter y1 = "))
	'''print("Enter the boundary values for window :")
	xwmin = int(input("min x-coordinate :"))
	xwmax = int(input("max x-coordinate :"))
	ywmin = int(input("min y-coordinate :"))
	ywmax = int(input("max y-coordinate :"))
	print("Enter the boundary values for viewport :")
	xvmin = int(input("min x-coordinate :"))
	xvmax = int(input("max x-coordinate :"))
	yvmin = int(input("min y-coordinate :"))
	yvmax = int(input("max y-coordinate :"))'''			
	win = GraphWin("Line using Bresenham's Algorithm for line scanning by YUKTI",xvmax-xvmin,yvmax-yvmin)
	win.setBackground("light blue")
	win.setCoords(xvmin,yvmin,xvmax,yvmax)
	#x-axis
	l1 = Line(Point(-xvmax,0) , Point(xvmax,0))
	l1.draw(win)
	l1.setOutline("blue")
	#y-axis
	l2 = Line(Point(0,yvmax) , Point(0, -yvmax))
	l2.draw(win)
	l2.setOutline("blue")	
	t=Text(Point(xvmax-70,-20),"X-Axis")
	t.draw(win)
	t.setTextColor('blue')
	t=Text(Point(-60,yvmax-70),"Y-Axis")
	t.draw(win)
	t.setTextColor('blue')
	t=Text(Point(0,0),"(0,0)")
	t.draw(win)	
	
	#calling bresenham line algo function
	bresenham(x0,y0,x1,y1,win)				
	win.getMouse()	
	win.close()
	

main()


