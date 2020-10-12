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



def drawSymmetry(x,y,r,xi,yi,win):
	p1 = Point(transformX(x+xi),transformY(y+yi))
	p1.draw(win)
	p1.setFill('purple')
	p2 = Point(transformX(x+yi),transformY(y+xi))
	p2.draw(win)
	p2.setFill('purple')
	p3 = Point(transformX(x+yi),transformY(y-xi))
	p3.draw(win)
	p3.setFill('purple')	
	p4 = Point(transformX(x+xi),transformY(y-yi))
	p4.draw(win)
	p4.setFill('purple')	
	p5 = Point(transformX(x-xi),transformY(y-yi))
	p5.draw(win)
	p5.setFill('purple')	
	p6 = Point(transformX(x-yi),transformY(y-xi))
	p6.draw(win)
	p6.setFill('purple')	
	p7 = Point(transformX(x-yi),transformY(y+xi))
	p7.draw(win)
	p7.setFill('purple')	
	p8 = Point(transformX(x-xi),transformY(y+yi))
	p8.draw(win)
	p8.setFill('purple')


def drawCircle(cx,cy,r,win):
	c1 = transformX(cx)
	c2 = transformY(cy)
	print("The viewport coordinates of centre : ","(",c1,",",c2,")")
	m = Text(Point(c1,c2), "(%d,%d)"%(c1,c2))
	m.setTextColor("purple")
	m.setSize(10)
	m.draw(win)
	p = Point(c1,c2)
	p.draw(win)
	x,y = 0,r
	d = 1.25-r
	while(x<y):
		drawSymmetry(cx,cy,r,x,y,win)
		time.sleep(0.003)
		x+=1
		if (d < 0):
			d+= 2*x+3
		else:
			y-=1
			d+= 2*(x-y)+5
		

def main():
	# default boundary values for window and viewport
	global xwmin,xwmax,xvmin,xvmax,ywmin,ywmax,yvmin,yvmax	
	xvmin = -450
	yvmin = -450
	xvmax = 450	
	yvmax = 450
	xwmin = -2000
	ywmin = -2000
	xwmax = 2000	
	ywmax = 2000	
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
	win = GraphWin("Circle using bresenham Algorithm",xvmax-xvmin,yvmax-yvmin)
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
	
	print("Enter the coordinates of center of the circle : ")	
	cx = int(input("x-coordinate: "))
	cy = int(input("y-coordinate: "))
	r = int(input("Enter the radius of the circle: "));
	#r = 100
	
	p = Point(cx,cy)
	p.draw(win)
	
	drawCircle(cx,cy,r,win)
	
	win.getMouse()
	win.close()

main()

