from graphics import *
from lib import *


def parametricClipping(x1,y1,x2,y2,win,color):
	# Line is degenerate so clip as a point
	if(x1 == x2 and y1 == y2):
		if( x1 < xmax and x1 > xmin and y1 > ymin and ymax > y1):
			print("Line is degenerate so clipped as a point")
			win.plot(x1,y1,color)
	else:
		te = 0.0
		tl = 1.0
		# left
		if (x2-x1 != 0):
			t = (x1-xmin)/(x1-x2)
			print(t)
			if (-(x2-x1)<0):
				te = max(te,t)
			else:
				tl = min(tl,t)
		# bottom
		if (y2-y1 != 0):
			t = (y1-ymin)/(y1-y2)
			print(t)
			if (-(y2-y1)<0):
				te = max(te,t)
			else:
				tl = min(tl,t)

		# top
		if (y2-y1 != 0):
			t = (y1-ymax)/(y1-y2)
			print(t)
			if (y2-y1) < 0:
				te = max(te,t)
			else:
				tl = min(tl,t)

		#right
		if (x2-x1 != 0):
			t = (x1-xmax)/(x1-x2)
			print(t)
			if (x2-x1)<0:
				te = max(te,t)
			else:
				tl = min(tl,t)

	if (te > tl):
		print("No Clipping can be done!")
		return win
	else:
		print(te,tl)
		x0,y0 = x1,y1	
		x3,y3  = x2,y2	
		x1 = x0 + (x3-x0)*te
		y1 = y0 + (y3-y0)*te
		x2 = x0 + (x3-x0)*tl
		y2 = y0 + (y3-y0)*tl

		x1 = int(x1)
		x2 = int(x2)
		y1 = int(y1)
		y2 = int(y2)
		print(x1,y1)
		print(x2,y2)
		l1 = Text(Point(x1,y1),'('+str(x1)+ ','+str(y1)+ ')')
		l1.draw(win)	
		l2 = Text(Point(x2,y2),'('+str(x2)+ ','+str(y2)+ ')')
		l2.draw(win)		
		win = line(x1,y1,x2,y2,win,color)
		return win       
               

def main():
	global xmin,xmax,ymin,ymax
	win = GraphWin("PARAMETRIC LINE CLIPPING ALGORITHM",900,900)
	win.setCoords(-450,-450,450,450)	
	win = drawAxis(win)
	print("Enter the rectangular region : ")
	xmin = int(input("Enter the min x-coordinate = "))
	xmax = int(input("Enter the max x-coordinate = "))
	ymin = int(input("Enter the min y-coordinate = "))
	ymax = int(input("Enter the max y-coordinate = "))	
	
	Points = [(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax),(xmin,ymin)]
	win = drawPolygon(4,Points,win,"purple")
	
	print("Enter the end point-1 of the line : ")
	x1 = int(input("Enter x1 : "))
	y1 = int(input("Enter y1 : "))
	
	print("Enter the end points-2 of the line : ")
	x2 = int(input("Enter x2 : "))
	y2 = int(input("Enter y2 : "))
	
	l1 = Text(Point(x1,y1),'('+str(x1)+ ','+str(y1)+ ')')
	l2 = Text(Point(x2,y2),'('+ str(x2)+ ','+str(y2)+ ')')
	l1.draw(win)
	l2.draw(win)	
	
	win = line(x1,y1,x2,y2,win,"red")
	
	win = parametricClipping(x1,y1,x2,y2,win,"green")
	win.getMouse()
	win.close()

main()