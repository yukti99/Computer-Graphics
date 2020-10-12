# PARALLEL-ORTHOGRAPHIC PROJECTION ON AN ARBITRARY PLANE IN 3-D COORDINATE SYSTEM

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

def projectionPoints(v):
	P = []
	for i in range(len(v)):
		x,y,z = v[i]
		x = (x*(d1-a*n1)- y*a*n2 - z*a*n3 + a*d0)/d1
		y = (-x*b*n1+ y*(d1-b*n2)- z*b*n3 + b*d0)/d1
		z = (-x*c*n1 - y*c*n2+ z*(d1-c*n3)+ c*d0)/d1
		P.append([x,y,z])
	return P


def ap():
	global a,b,c,d0,d1,n1,n2,n3
	win = GraphWin("PARALLEL-ORTHOGRAPHIC PROJECTION ON ARBITRARY PLANE ",900,900)
	win.setCoords(-500,-500,500,500)	
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

	# the reference point lying on the arbitrary plane
	pt = f.readline().strip('\n').split(" ")
	x0,y0,z0 = int(pt[0]),int(pt[1]),int(pt[2])

	# The normal of arbitrary plane 
	pt = f.readline().strip('\n').split(" ")
	n1,n2,n3 = int(pt[0]),int(pt[1]),int(pt[2])

	# The direction vector of projection 
	#pt = f.readline().strip('\n').split(" ")
	#a,b,c = int(pt[0]),int(pt[1]),int(pt[2])
	# translation 

	a,b,c = -n1,-n2,-n3 # since projection is orthogonal 
	d1 = a*n1 + b*n2 + c*n3
	d0 = n1*x0 + n2*y0 + n3*z0

	P1 = projectionPoints(v1)
	P2 = projectionPoints(v2)	

	print(P1)
	print(P2)

	# now v1 and v2 represents parallel orthogonal projections
	win = drawFigure(no,P1,P2,win)
	print("\n*************************************************************")
	print("Mouse Click on the Graphics Window to continue !!!")
	print("*************************************************************\n")
	win.getMouse()
	win.close()


