# PARALLEL-ORTHOGRAPHIC PROJECTION IN 3-D COORDINATE SYSTEM

from graphics import *
from math import *
import numpy as np


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

def drawLine(x1,y1,z1,x2,y2,z2,win,color):
	a = x1-(z1*0.4)
	b = y1-(z1*0.4)
	c = x2-(z2*0.4)
	d = y2-(z2*0.4)	
	line = Line(Point(a,b),Point(c,d));
	line.setFill(color)
	line.setWidth(2)
	line.draw(win)
	return win 

def drawFigure(no,v1,v2,win):
	k=0
	colors = ["purple","yellow","pink","darkcyan","darkgoldenrod","magenta","darkgreen","black","orangered","darkgrey","saddlebrown","midnightblue","red","coral","whitesmoke","navy"]
	for i in range(no):		
		x1,y1,z1 = v1[i][0],v1[i][1],v1[i][2]
		x2,y2,z2 = v2[i][0],v2[i][1],v2[i][2]
		k = (k+1)%len(colors)
		win = drawLine(x1,y1,z1,x2,y2,z2,win,colors[k])
	return win


def Translate(v,Tx,Ty,Tz):
	T = [[1,0,0,0],
		[0,1,0,0],
		[0,0,1,0],
		[Tx,Ty,Tz,1]]
	P = []
	for i in v:
		x,y,z = i
		prod = np.dot([x,y,z,1],T)
		P.append([prod[0],prod[1],prod[2]])
	return P

def Scale(v):
	S = [[Sx,0,0,0],
		[0,Sy,0,0],
		[0,0,Sz,0],
		[Sx,Sy,Sz,1]]
	P = []
	for i in v:
		x,y,z = i
		prod = np.dot([x,y,z,1],S)
		P.append([prod[0],prod[1],prod[2]])
	return P

def Rotate(v,angle,axis,direction):
	if (direction == 1):
		angle = -angle
	c = cos(angle)
	s = sin(angle)
	Tx = [[1,0,0,0],
	      [0,c,s,0],
	      [0,-s,c,0],
	      [0,0,0,1]]
	Ty = [[c,0,-s,0],
		  [0,1,0,0],
		  [-s,0,c,0],
		  [0,0,0,1]]
	Tz = [[c,s,0,0],
		  [-s,c,0,0],
		  [0,0,1,0],
		  [0,0,0,1]]

	if (axis==1):
		T = Tx
	elif (axis==2):
		T = Ty
	else:
		T = Tz

	P = []
	for i in v:
		x,y,z = i
		prod = np.dot([x,y,z,1],T)
		P.append([prod[0],prod[1],prod[2]])
	return P


def Reflect(v):
	if (about == 1):
		# xy plane 
		T = [[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]]
	elif (about == 2):
		# yz plane 
		T = [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
	elif (about == 3):
		# zx plane 
		T = [[1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]]
	else:
		# about origin
		T = [[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]]
	P = []
	for i in v:
		x,y,z = i
		prod = np.dot([x,y,z,1],T)
		P.append([prod[0],prod[1],prod[2]])
	return P

def Shear(v):
	if (sp == 1):
		# xy plane 
		S = [[1,0,0,0],[0,1,0,0],[a,b,1,0],[0,0,0,1]]
	elif (sp == 2):
		# yz plane 
		S = [[1,a,b,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
	elif (sp == 3):
		# zx plane 
		S = [[1,0,0,0],[a,1,b,0],[0,0,1,0],[0,0,0,1]]
	P = []
	for i in v:
		x,y,z = i
		prod = np.dot([x,y,z,1],S)
		P.append([prod[0],prod[1],prod[2]])
	return P

def rotateAboutAxis(v,angle,axis):
	x1,y1,z1,x2,y2,z2 = axis	
	A = x2-x1
	B = y2-y1
	C = z2-z1
	Tx = -x1;
	Ty = -y1
	Tz = -z1
	polygon = Translate(v,Tx,Ty,Tz)	
	L = sqrt(A*A + B*B + C*C)
	V = sqrt(B*B + C*C)
	temp1 = B/V
	angle1 = asin(temp1)
	angle1 = degrees(angle1)
	P = Rotate(v,angle1,1,0)
	temp2 = V/L
	angle2 = acos(temp2)
	angle2 = degrees(angle2)
	P = Rotate(P,angle2,2,1)
	P = Rotate(P,angle2,3,0)
	P = Rotate(P,angle2,2,0)
	P = Rotate(P,angle2,1,1)
	Tx = x1
	Ty = y1
	Tz = z1
	P = Translate(P,Tx,Ty,Tz)
	return P		
	

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    return win


def main():
	global v1,v2,no,Sx,Sy,Sz,about,sp,a,b
	# take input from input file 
	f = open("transform.txt")
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
	

	while(True):		

		print("\n*************************************************************")
		print("\nWELCOME TO 3-D TRANSFORMATION\n")
		print("PRESS 1 for TRANSLATION !")
		print("PRESS 2 for SCALING !")
		print("PRESS 3 for ROTATION !")
		print("PRESS 4 for SHEAR TRANSFORMATION !")
		print("PRESS 5 for REFLECTION !")
		print("PRESS 6 for ROTATION ABOUT AN AXIS !")
		print("PRESS 7 for EXIT !")
		print("*************************************************************\n")

		c = int(input("Enter your choice: "))



		if (c == 1):
			win = GraphWin("3-D TRANSFORMATION",900,900)
			win.setCoords(-500,-500,500,500)
			drawAxis(win)		
			win = drawFigure(no,v1,v2,win)
			print("\nEnter the translation factors Tx,Ty and Tz : ")
			Tx = int(input("Enter Tx = "))	
			Ty = int(input("Enter Ty = "))
			Tz = int(input("Enter Tz = "))
			P1 = Translate(v1,Tx,Ty,Tz)	
			P2 = Translate(v2,Tx,Ty,Tz)	
			win = drawFigure(no,P1,P2,win)
			print("Mouse Click to continue !!!")
			win.getMouse()
			win.close()
			

		elif (c==2):
			win = GraphWin("3-D TRANSFORMATION",900,900)
			win.setCoords(-500,-500,500,500)
			drawAxis(win)		
			win = drawFigure(no,v1,v2,win)
			print("Enter the translation factors Sx,Sy and Sz : ")
			Sx = int(input("Enter Sx = "))	
			Sy = int(input("Enter Sy = "))
			Sz = int(input("Enter Sz = "))
			P1 = Scale(v1)
			P2 = Scale(v2)
			win = drawFigure(no,P1,P2,win)
			print("Mouse Click to continue !!!")
			win.getMouse()
			win.close()

		elif (c==3):
			win = GraphWin("3-D TRANSFORMATION",900,900)
			win.setCoords(-500,-500,500,500)
			drawAxis(win)		
			win = drawFigure(no,v1,v2,win)
			angle = radians(int(input("Enter the angle of rotation = ")))
			print("Select the plane for projection: ")
			print("X Axis -> 1")
			print("Y Axis -> 2")
			print("Z Axis -> 3")

			axis = int(input("Enter the axis about which you want to rotate = "))
			direction = int(input("Enter direction:  clockwise(1) / anticlockwise(2) =  "))
			P1 = Rotate(v1,angle,axis)
			P2 = Rotate(v2,angle,axis)
			win = drawFigure(no,P1,P2,win)
			print("Mouse Click to continue !!!")
			win.getMouse()
			win.close()

		elif (c==4):
			win = GraphWin("3-D TRANSFORMATION",900,900)
			win.setCoords(-500,-500,500,500)
			drawAxis(win)		
			win = drawFigure(no,v1,v2,win)
			print("Enter shear factors: ")
			a = int(input("a = "))
			b = int(input("b = "))
			print("X-Y Plane -> 1")
			print("Y-Z Plane -> 2")
			print("X-Z Plane -> 3")
			print("ORIGIN    -> 4")
			sp = int(input("Shearing about which plane ? : "))
			P1 = Shear(v1)
			P2 = Shear(v2)
			win = drawFigure(no,P1,P2,win)
			print("Mouse Click to continue !!!")
			win.getMouse()
			win.close()

		elif (c==5):
			win = GraphWin("3-D TRANSFORMATION",900,900)
			win.setCoords(-500,-500,500,500)
			drawAxis(win)		
			win = drawFigure(no,v1,v2,win)
			print("X-Y Plane -> 1")
			print("Y-Z Plane -> 2")
			print("X-Z Plane -> 3")
			print("ORIGIN    -> 4")
			about = int(input("Reflection about which plane ? : "))

			P1 = Reflect(v1)
			P2 = Reflect(v2) 
			win = drawFigure(no,P1,P2,win)
			print("Mouse Click to continue !!!")
			win.getMouse()
			win.close()

		elif(c==6):
			win = GraphWin("3-D TRANSFORMATION",900,900)
			win.setCoords(-500,-500,500,500)
			drawAxis(win)		
			win = drawFigure(no,v1,v2,win)
			print("")
			angle = radians(int(input("Enter the angle of rotation = ")))
			print("Enter the end points of the axis about which you want to rotate: ")
			axis = list(map(int,input().strip("\n").split()))
			print(axis)
			P1 = rotateAboutAxis(v1,angle,axis)
			P2 = rotateAboutAxis(v2,angle,axis)
			win = drawFigure(no,P1,P2,win)
			print("Mouse Click to continue !!!")
			win.getMouse()
			win.close()
		elif (c==7):
			print("Thank you bye!\n")
			break

		else:
			print("Sorry! Wrong Option...")
		
		
	
	

main()