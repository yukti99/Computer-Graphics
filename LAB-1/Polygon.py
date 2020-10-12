from graphics import *

def line(x0,y0,x1,y1,win):
	dx = x1 - x0
	dy = y1 - y0
	xsign,ysign = 1,1	
	if (dx < 0):
		xsign=-1
	if(dy < 0):
		ysign=-1
	dx = abs(dx)
	dy = abs(dy)
	if (dx > dy):
		xx=xsign
		xy=0
		yx=0
		yy=ysign
	else:
		dx,dy=dy,dx
		xx=0
		xy=ysign
		yx=xsign
		yy=0
	D = 2*dy - dx
	y = 0
	for x in range(dx + 1):
		a = x0 + x*xx + y*yx
		b = y0 + x*xy + y*yy
		p = Point(a,b)
		p.draw(win)
		p.setFill('purple')		
		time.sleep(0.003)	
		if (D >= 0):
			y += 1
			D -= 2*dx
		D += 2*dy		

def drawPolygon(n,Points,win):
	for i in range(n):		
		x1,y1 = Points[i]
		x1,y1 = transformX(x1),transformY(y1)
		p = Point(x1,y1)
		print("The viewport coordinates of point %d : "%(i+1),"(",x1,",",y1,")")
		p.setFill('purple')
		p.draw(win)
		t=Text(Point(x1,y1),"(%d,%d)"%(x1,y1))		
		t.setTextColor('purple')
		t.draw(win)		
		x2,y2 = Points[i+1]
		x2,y2 = transformX(x2),transformY(y2)	
		line(x1,y1,x2,y2,win)
		

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
	
	n = int(input("Enter the no of points in polygon: "))
	Points=[]
	for i in range(n):
		print("Enter Point ",i+1,": ")
		x = int(input("x-coordinate: "))
		y = int(input("y-coordinate: "))
		Points.append((x,y))
	#Points = sorted(Points , key=lambda k: [k[1], k[0]])
	
	Points.append((Points[0][0],Points[0][1]))			
	win = GraphWin("Polygon",xvmax-xvmin,yvmax-yvmin)
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
	
	
	
	drawPolygon(n,Points,win)
	
	win.getMouse()
	win.close()

main()
  

