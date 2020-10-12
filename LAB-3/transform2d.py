""" PLEASE COMPILE WITH : sudo python3 transform2d.py  """

"""YUKTI KHURANA - 2017UCP1234"""

from graphics import *
import sys
import numpy as np 
import keyboard
from math import *

xvmin = -450
yvmin = -450
xvmax = 450	
yvmax = 450
xwmin = -2000
ywmin = -2000
xwmax = 2000	
ywmax = 2000

def line(x0,y0,x1,y1,win,color):
	dx = int(x1 - x0)
	dy = int(y1 - y0)
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
		win.plot(a,b,color)	
		if (D >= 0):
			y += 1
			D -= 2*dx
		D += 2*dy
	return win		

def drawPolygon(n,Points,win,color):
	for i in range(n):		
		x1,y1 = Points[i]		
		x2,y2 = Points[i+1]
		win = line(x1,y1,x2,y2,win,color)
	return win


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



def matrix(x,y,initial):
	return [[initial for i in range(x)] for j in range(y)]

def mult(a,b):
	return np.dot(a,b)

def tranxMatrix(tx,ty):
	return [[1,0,0],
			[0,1,0],
			[tx,ty,1]]

def Rz(a):
	return [[cos(a),sin(a),0],
			[-sin(a),cos(a),0],
			[0,0,1]]
def Ry(a):
	return [[cos(a),0,sin(a)],
			[0,0,1],
			[-sin(a),0,cos(a)]
			]
def Rx(a):
	return [[1,0,0],
			[0,cos(a),-sin(a)],
			[0,sin(a),cos(a)]]

def scaleMatrix(sx,sy):
	return [[sx,0,0],
			[0,sy,0],
			[0,0,1]]

def refx():
	return [[1,0,0],[0,-1,0],[0,0,1]]
def refy():
	return [[-1,0,0],[0,1,0],[0,0,1]]
def refo():
	return [[-1,0,0],[0,-1,0],[0,0,1]]
def shearX(s):
	return [[1,0,0],[s,1,0],[0,0,1]]
def shearY(s):
	return [[1,s,0],[0,1,0],[0,0,1]]



def translate(sides,Points,tx,ty,win):
	P = matrix(3,sides,1)
	for i in range(sides):
		P[i][0],P[i][1] = Points[i][0],Points[i][1]
	T = tranxMatrix(tx,ty)
	r = mult(P,T)
	Q = []
	for i in range(sides):		
		x,y = r[i][0],r[i][1]
		Q.append((x,y))
	xi,yi,zi = r[0]

	Q.append((xi,yi))
	return Q
	

def Rotate(sides,Points,a,axis,win):
	P = matrix(3,sides,1)
	for i in range(sides):
		P[i][0],P[i][1] = Points[i][0],Points[i][1]
	if (axis=="x"):
		T = Rx(a)
	elif (axis == "y"):
		T = Ry(a)
	else:
		T = Rz(a)
	r = mult(P,T)
	Q = []
	for i in range(sides):		
		x,y = r[i][0],r[i][1]
		Q.append((x,y))
	xi,yi,zi = r[0]
	Q.append((xi,yi))
	return Q
	

def Scale(sides,Points,sx,sy,win):
	P = matrix(3,sides,1)
	for i in range(sides):
		P[i][0],P[i][1] = Points[i][0],Points[i][1]
	#print(P)
	T = scaleMatrix(sx,sy)
	#print(T)
	r = mult(P,T)
	#print(r)
	Q = []
	for i in range(sides):		
		x,y = r[i][0],r[i][1]
		Q.append((x,y))
	xi,yi,zi = r[0]
	Q.append((xi,yi))
	#print(Q)
	return Q

def Reflect(sides,Points,about,win):
	P = matrix(3,sides,1)
	#print(P)
	for i in range(sides):
		P[i][0],P[i][1] = Points[i][0],Points[i][1]
	#print(P)
	if (about == "x"):
		T = refx()
	elif (about == "y"):
		T = refy()
	else:
		T = refo()
	#print(T)
	r = mult(P,T)
	#print(r)
	Q = []
	for i in range(sides):		
		x,y = r[i][0],r[i][1]
		Q.append((x,y))
	xi,yi,zi = r[0]
	Q.append((xi,yi))
	#print(Q)
	return Q

def Shearing(sides,Points,about,s,win):
	P = matrix(3,sides,1)
	#print(P)
	for i in range(sides):
		P[i][0],P[i][1] = Points[i][0],Points[i][1]
	#print(P)
	if (about == "x"):
		T = shearX(s)
	else:
		T = shearY(s)
	
	#print(T)
	r = mult(P,T)
	#print(r)
	Q = []
	for i in range(sides):		
		x,y = r[i][0],r[i][1]
		Q.append((x,y))
	xi,yi,zi = r[0]
	Q.append((xi,yi))
	#print(Q)
	return Q
	
def angle_trunc(a):
    while a < 0.0:
        a += 3.14 * 2
    return a

def main():
	
	global xmin,xmax,ymin,ymax,clipWindow,sides
	win = GraphWin("TRANSFORMATIONS IN 2-D",900,900)
	win.setCoords(-450,-450,450,450)	
	win = drawAxis(win)

	# draw polygon
	sides=int(input("Enter number of sides of polygon = "))
	Points = []
	for i in range(sides):		
		x = int(input("Enter x : "))
		y = int(input("Enter y : "))
		Points.append((x,y))
	xi,yi = Points[0]
	Points.append((xi,yi))
	"""
	FOR INPUT 
	Points = [(100,300),(500,100),(100,100),(100,300)]
	sides = 3
	tx = -100
	ty = -100
	angle = radians(-45)
	drawPolygon(sides,Points,win,"red")
	Q  = translate(sides,Points,tx,ty,win)
	drawPolygon(sides,Q,win,"green")
	Q = Rotate(sides,Q,-angle,"z",win)
	drawPolygon(sides,Q,win,"blue")
	Q = Reflect(sides,Q,"x",win)
	drawPolygon(sides,Q,win,"yellow")
	Q = Rotate(sides,Q,angle,"z",win)
	drawPolygon(sides,Q,win,"black")
	Q = translate(sides,Q,-tx,-ty,win)
	drawPolygon(sides,Q,win,"purple")
	sides = 4
	Points = [(500,500),(500,200),(200,200),(200,500),(500,500)]"""
	drawPolygon(sides,Points,win,"red")
	print("\n\nWELCOME TO 2-D TRANSFORMATION\n\n")
	print("PRESS t for TRANSLATION !")
	print("PRESS shift+t for  INVERSE TRANSLATION !")
	print("PRESS r for ROTATION !")
	print("PRESS s for SCALING !")
	print("PRESS a for REFLECTION  !")
	print("PRESS h for SHEAR TRANSFORMATION  !")
	print("PRESS y for REFLECTION ABOUT A LINE\n\n")
	

	#HERE REFERENCE POINT IS CONSIDERED ONE OF THE VERTEX OF POLYGON WHILE TRANSFORMING 
	
	while True:
	        if keyboard.is_pressed('t'):

	        	tx = (input("Enter the Tx value : "))
	        	tx = int(tx[1:])
	        	ty = int(input("Enter the Ty value : "))
	        	print(tx,ty)
	        	Q = translate(sides,Points,tx,ty,win)	
	        	drawPolygon(sides,Q,win,"purple")
	        	break

	        if keyboard.is_pressed('shift+t'):
	        	tx = (input("Enter the Tx value : "))
	        	tx = int(tx[1:])
	        	ty = int(input("Enter the Ty value : "))
	        	print(-tx,-ty)
	        	Q = translate(sides,Points,-tx,-ty,win)	
	        	drawPolygon(sides,Q,win,"purple")
	        	break

	        if keyboard.is_pressed('r'):
	        	a = (input("Enter the angle value : "))
	        	a = int(a[1:])
	        	wise = input("Anti-clockwise - a /clockwise - c ? = ")
	        	if (wise == 'c'):
	        		a = -a
	        	axis = str(input("About which axis ? (x/y/z) = "))  
	        	Q = translate(sides,Points,-Points[0][0],-Points[0][1],win)
	        	#drawPolygon(sides,Q,win,"green")
	        	Q = Rotate(sides,Q,radians(a),axis,win)
	        	#drawPolygon(sides,Q,win,"green")
	        	Q = translate(sides,Q,Points[0][0],Points[0][1],win)
	        	drawPolygon(sides,Q,win,"purple")
	        	break 

	        if keyboard.is_pressed('s'):
	        	sx = (input("Enter the Sx value : "))
	        	sx = int(sx[1:])
	        	sy = int(input("Enter the Sy value : "))
	        	print(sx,sy)
	        	Q = translate(sides,Points,-Points[0][0],-Points[0][1],win)
	        	#drawPolygon(sides,Q,win,"green")
	       		Q = Scale(sides,Q,sx,sy,win)
	       		#drawPolygon(sides,Q,win,"blue")
	       		Q = translate(sides,Q,Points[0][0],Points[0][1],win)
	       		drawPolygon(sides,Q,win,"purple")
	       		Scale(sides,Points,sx,sy,win)	
	       		break

	       	if keyboard.is_pressed('a'):
	        	tx = (input("Reflection about x-axis (x)/y-axis(y)/origin(o) : "))
	        	tx = tx[1:]
	        	Q = Reflect(sides,Points,tx,win)	
	        	drawPolygon(sides,Q,win,"purple")
	        	break

	        if keyboard.is_pressed('h'):
	        	tx = (input("Shearing about x-axis (x)/y-axis(y) : "))
	        	tx = tx[1:]
	        	s = int(input("Enter the Shear value : "))
	        	Q = translate(sides,Points,-Points[0][0],-Points[0][1],win)
	        	Q = Shearing(sides,Q,tx,s,win)	
	        	Q = translate(sides,Q,Points[0][0],Points[0][1],win)
	        	drawPolygon(sides,Q,win,"purple")
	        	break

	        if keyboard.is_pressed('y'):
	        	print("\nEnter the end points of line : \n")
	        	x0 = (input("Enter x0 = "))
	        	x0 = int(x0[1:])
	        	y0 = int(input("Enter y0 = "))
	        	print(x0,y0)
	        	
	        	x1 = int(input("Enter x1 = "))
	        	y1 = int(input("Enter y1 = "))
	        	print(x1,y1)
	        	win = line(x0,y0,x1,y1,win,"black")
	        	x2 = int(x1-x0)
	        	y2 = int(y1-y0)
	        	if (x2!=0):
	        		slope = y2/x2
	        		tx = 0  
	        		ty = y0 - slope*x0
	        	else:
	        		slope = sys.maxsize
	        		ty = 0
	        		tx = x0
	        	print(tx,ty)
	        	temp = (x2)/sqrt(x2*x2 + y2*y2)
	        	if(temp<0):
	        		temp = -temp
	        	angle = acos(temp)
	        	angle = degrees(angle)
	        	if (x1 >= 0 and y1<=0) or (x1<=0 and y1>=0):
	        		angle = -angle		        	
	        	#print("angle = ",angle)
	        	angle = radians(angle)
	        	print("ANGLE OF ROTATION TO MAKE IT PRINCIPLE AXIS-X = ",angle)
	        	Q = translate(sides,Points,-x1,-y1,win)
	        	Q = Rotate(sides,Q,-angle,"z",win)
	        	Q = Reflect(sides,Q,"x",win)
	        	Q = Rotate(sides,Q,angle,"z",win)
	        	Q = translate(sides,Q,x1,y1,win)
	        	drawPolygon(sides,Q,win,"purple")       
	        	break

	       
	        if keyboard.is_pressed('q'): 
	        	win.close() 
	        	exit()
	        	break

	win.getMouse()
	win.close()

main()


"""YUKTI KHURANA - 2017UCP1234"""
