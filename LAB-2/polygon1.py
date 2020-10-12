from graphics import *

boundary_values = []
xvmin = -450
yvmin = -450
xvmax = 450	
yvmax = 450
xwmin = -2000
ywmin = -2000
xwmax = 2000	
ywmax = 2000

def line(x0,y0,x1,y1,win,color):
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
		#p = Point(a,b)
		#p.draw(win)
		# to keep track of boundary coordinates of the polygon
		boundary_values.append((a,b))
		#p.setFill(color)		
		#time.sleep(0.003)
		win.plot(a,b,color)	
		if (D >= 0):
			y += 1
			D -= 2*dx
		D += 2*dy
	return win		

def drawPolygon(n,Points,win,color):
	for i in range(n):		
		x1,y1 = Points[i]
		x1,y1 = transformX(x1),transformY(y1)		
		x2,y2 = Points[i+1]
		x2,y2 = transformX(x2),transformY(y2)	
		win = line(x1,y1,x2,y2,win,color)
	return win
	
def transformX(xw):
	t = (xvmax-xvmin)/(xwmax-xwmin)
	xv = xvmin + ((xw-xwmin)*t)
	return int(xv)
	
def transformY(yw):
	t = (yvmax-yvmin)/(ywmax-ywmin)
	yv = yvmin + ((yw-ywmin)*t)
	return int(yv)
	
def drawAxis(win):
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
	return win	
	



