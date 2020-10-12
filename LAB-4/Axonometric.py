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


def projectionPoints(v,a,b,c):
		P = []
		for i in v:
			x,y,z = i
			t = -(a*x+b*y+c*z)/(a*a+b*b+c*c)
			x += a*t
			y += b*t
			z += c*t
			P.append([x,y,z])
		return P

def ax():
	global v1,v2,no,Txy,Tyz,Txz
	win = GraphWin("AXONOMETRIC PROJECTION",900,900)
	win.setCoords(-500,-500,500,500)	
	win.setBackground("white")
	drawAxis(win)
	# take input from input file 
	#f = open("axo.txt")
	f = open("inputProjections.txt")
	no = int(f.readline().strip("\n"))
	# list of all vertices 
	v1 = []
	v2 = []		
	i=0
	
	while(i!=no):
		pt = f.readline().strip('\n').split(" ")
		x,y,z = int(pt[0]),int(pt[1]),int(pt[2])
		x1,y1,z1 = int(pt[3]),int(pt[4]),int(pt[5])
		v1.append([x,y,z])
		v2.append([x1,y1,z1])
		i+=1

	win = drawFigure(no,v1,v2,win)
		
	# translation factor
	pt = f.readline().strip('\n').split(" ")
	tx,ty,tz = int(pt[0]),int(pt[1]),int(pt[2])
	ShiftV(v1,tx,ty,tz)
	ShiftV(v2,tx,ty,tz)

	print("Select type of Axonometric projection : ")
	print("ISOMETRIC-> i")
	print("DIMETRIC -> d")
	print("TRIMETRIC-> t")
	print("BACK TO MAIN MENU OF PROJECTIONS -> b")
	type = input("Enter your choice (i/d/t/b) = ")
	"""
    NOTE: DIRECTION d for each of isometric, dimetric and trimetric can be changed 
    	by changing a,b,c given below
	"""
	if (type == "b"):
		win.close()
		return # return to main menu
	elif (type == "d"):
		"""a = 1
		b = 6
		d = 2*a+b
		Td = [
			 [(a+b) ,-a    ,-b   ,0],
			 [-a    ,(a+b) ,-b   ,0],
			 [-a    ,-a    ,(2*a),0],
			 [ 0    , 0    , 0   ,1]
			 ]"""
		print("DIMETRIC PROJECTION")
		x = int(input("Enter the equal value for dimetric = "))
		y = int(input("Enter the different value for trimetric = "))
		print("Select the two axis with which it makes equal angles (xy->1 or yz->2 or xz->3): ")
		axis = int(input())
		if(axis==1):
			a = x
			b = x
			c = y
		elif(axis==2):
			a = y
			b = x
			c = x
		elif(axis==3):
			a = x
			c = x
			b = y	
		#ShiftV(v1,0,0,-100)
		#ShiftV(v2,0,0,-100)
		P1 = projectionPoints(v1,a,b,c)
		P2 = projectionPoints(v2,a,b,c)

	elif (type == "t"):
		print("TRIMETRIC PROJECTION")
		"""a = 7
		b = 6
		c = 12
		d = a+b+c
		Tt = [
			 [b+c ,-b  ,-c , 0],
			 [-a  ,a+c ,-c , 0],
			 [-a  ,-b  ,a+b, 0],
			 [ 0  , 0  ,0  , 1]
			 ]"""
		#ShiftV(v1,0,0,-100)
		#ShiftV(v2,0,0,-100)
		print("Enter projection plane direction: ")
		a = int(input("Enter a = "))
		b = int(input("Enter b = "))
		c = int(input("Enter c = "))
		P1 = projectionPoints(v1,a,b,c)
		P2 = projectionPoints(v2,a,b,c)
	else:
		if (type!="i"):
			print("You have entered the wrong choice by mistable so, by default this is : ")
		print("ISOMETRIC PROJECTION")
		# isometric projection for d=(1,1,1) onto z plane 
		Tiso = [[2/3,-1/3,1/3,0],
				[-1/3,2/3,-1/3,0],
				[-1/3,-1/3,2/3,0],
				[ 0 , 0, 0,1]]
		#ShiftV(v1,40,40,40)
		#ShiftV(v2,40,40,40)
		d=1 # by default 
		d = int(input("Enter the direction vector for isometric (d,d,d) = "))
		P1 = projectionPoints(v1,d,d,d)
		P2 = projectionPoints(v2,d,d,d)

	win = drawFigure(no,P1,P2,win)	
	print("\n*************************************************************")
	print("Mouse Click on the Graphics Window to continue !!!")
	print("*************************************************************\n")
	win.getMouse()
	win.close()



