# PARALLEL-OBLIQUE PROJECTION - CABINET & CAVALIER IN 3-D COORDINATE SYSTEM

from graphics import *
import numpy as np 
from math import *

# draw the 3-D coordinate axis 
def drawAxis(win):
	xaxis=Line(Point(-500,0),Point(500,0)) 
	yaxis=Line(Point(0,-500),Point(0,500))
	zaxis=Line(Point(300,300),Point(-500,-500)) 
	xaxis.setOutline("Blue") 
	yaxis.setOutline("Blue")
	zaxis.setOutline("Blue")
	xaxis.draw(win)
	yaxis.draw(win)
	zaxis.draw(win)
	xaxis.setArrow('both')
	yaxis.setArrow('both')
	zaxis.setArrow('both')
	t=Text(Point(500-70,-20),"X-Axis")
	t.draw(win)
	t.setTextColor('blue')
	t=Text(Point(-60,500-70),"Y-Axis")
	t.draw(win)
	t.setTextColor('blue')
	t=Text(Point(-430,-380),"Z-Axis")
	t.draw(win)
	t.setTextColor('blue')
	t=Text(Point(0,0),"(0,0)")
	t.draw(win)
	return win

def ShiftV(v,tx,ty,tz):
	for i in range(len(v)):
		v[i] = v[i][0]+tx,v[i][1]+ty,v[i][2]+tz

def drawLine(x1,y1,z1,x2,y2,z2,win,color):
	a = x1-(z1*0.3)
	b = y1-(z1*0.3)
	c = x2-(z2*0.3)
	d = y2-(z2*0.3)	
	line = Line(Point(a,b),Point(c,d));
	line.setFill(color)
	line.setWidth(2)
	line.draw(win)
	return win 


def drawFigure(no,v1,v2,win):
	k=0
	colors = ["purple","firebrick","pink","darkcyan","darkgoldenrod","magenta","darkgreen","black","orangered","darkgrey","saddlebrown","midnightblue","red","coral","whitesmoke","navy"]
	for i in range(no):		
		x1,y1,z1 = v1[i][0],v1[i][1],v1[i][2]
		x2,y2,z2 = v2[i][0],v2[i][1],v2[i][2]
		k = (k+1)%len(colors)
		win = drawLine(x1,y1,z1,x2,y2,z2,win,colors[k])
	return win

def projectionPoints(v,T):
		P = []
		for i in v:
			x,y,z = i
			prod = np.dot([x,y,z,1],T)
			P.append([prod[0],prod[1],prod[2]])
		return P

def Plane():
	print("Select the plane for projection: ")
	print("X-Y Plane -> 1")
	print("Y-Z Plane -> 2")
	print("X-Z Plane -> 3")
	plane = int(input("Enter the plane of projection code (1/2/3) : "))
	# drawing actual parallel-orthogonal projection
	if (plane == 1):
		T = Txy

	elif (plane == 2):
		T = Tyz
	else:
		T = Txz
	return T


def op():
	global v1,v2,no,Txy,Tyz,Txz
	win = GraphWin("PARALLEL-ORTHOGRAPHIC PROJECTION",900,900)
	win.setCoords(-500,-500,500,500)	
	win.setBackground("white")
	drawAxis(win)

	# take input from input file 
	f = open("project2.txt")
	no = int(f.readline().strip("\n"))
	# list of all vertices 
	v1 = []
	v2 = []		
	i=0
	#print("The 3-D coordinates of the Figure : ")
	while(i!=no):
		pt = f.readline().strip('\n').split(" ")
		x,y,z = int(pt[0]),int(pt[1]),int(pt[2])
		x1,y1,z1 = int(pt[3]),int(pt[4]),int(pt[5])
		v1.append([x,y,z])
		v2.append([x1,y1,z1])
		i+=1

	win = drawFigure(no,v1,v2,win)
	t=Text(Point(v1[0][0],v1[0][1]),"Fig1")
	t.setTextColor('blue')
	t.draw(win)

	"""
	THESE VALUES CAN BE CHANGED FROM THE FILE-> project2.txt

	"""
	# Translation factor
	pt = f.readline().strip('\n').split(" ")
	tx,ty,tz = int(pt[0]),int(pt[1]),int(pt[2])
	ShiftV(v1,tx,ty,tz)
	ShiftV(v2,tx,ty,tz)

	print("Select type of oblique projection : ")
	print("CAVALIER -> a")
	print("CABINET  -> b")
	print("BACK TO MAIN MENU OF PROJECTIONS -> c")
	type = input("Enter your choice (a/b/c) = ")
	if (type == "c"):
		win.close()
		return # return to main menu

	elif (type == "a"):
		print("CAVALIER PROJECTION")
		angleA = radians(45)
	else:
		if (type!="b"):
			print("You have entered the wrong choice by mistable so, by default this is : ")
		print("CABINET PROJECTION")
		print("Foreshortening occurs in Cabinet Projection")
		angleA = radians(63.4)

	
	angleB = radians(int(input("Enter the angle of projection on the plane for oblique- projection: ")))
	# Foreshortening factor 
	f = 1/tan(angleA)
	a = f*sin(angleB)
	b = f*cos(angleB)
	 

	Txy = [[1, 0, 0, 0],
		 [0, 1, 0, 0],
		 [a, b, 0, 0],
		 [0, 0, 0, 1]]

	Tyz =[[0, a, b, 0],
		 [0, 1, 0, 0],
		 [0, 0, 1, 0],
		 [0, 0, 0, 1]]

	Txz =[[1,0, 0, 0],
		 [a,0,b, 0],
		 [0, 0, 1, 0],
		 [0, 0, 0, 1]]

	T = Plane()

	P1 = projectionPoints(v1,T)
	P2 = projectionPoints(v2,T)

	win = drawFigure(no,P1,P2,win)
	print("\n*************************************************************")
	print("Mouse Click on the Graphics Window to continue !!!")
	print("*************************************************************\n")
	win.getMouse()
	win.close()

