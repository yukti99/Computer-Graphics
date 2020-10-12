# PARALLEL-ORTHOGRAPHIC PROJECTION IN 3-D COORDINATE SYSTEM

from graphics import *
import math

# using the logic
"""
for x-y plane:
	T = 1 0 0 0
		0 1 0 0 
		0 0 0 0
		0 0 0 1

"""
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

def ShiftV(v,tx,ty,tz):
	for i in range(len(v)):
		v[i] = [v[i][0]+tx,v[i][1]+ty,v[i][2]+tz]


def drawFigure(no,v1,v2,win):
	k=0
	colors = ["purple","firebrick","pink","darkcyan","darkgoldenrod","magenta","darkgreen","black","orangered","darkgrey","saddlebrown","midnightblue","red","coral","whitesmoke","navy"]
	for i in range(no):		
		x1,y1,z1 = v1[i][0],v1[i][1],v1[i][2]
		x2,y2,z2 = v2[i][0],v2[i][1],v2[i][2]
		k = (k+1)%len(colors)
		win = drawLine(x1,y1,z1,x2,y2,z2,win,colors[k])
	return win


def Plane():
	print("Select the plane for projection: ")
	print("X-Y Plane -> 1")
	print("Y-Z Plane -> 2")
	print("X-Z Plane -> 3")
	plane = int(input("Enter the plane of projection code (1/2/3) : "))
	# drawing actual parallel-orthogonal projection
	if (plane == 1):
		# X-Y PLANE, Z=0
		# set the z vertice of all vertices to 0
		for i in range(no):
			v1[i][2] = 0
			v2[i][2] = 0

	elif (plane == 2):
		# Y-Z PLANE, X=0
		# set the x vertice of all vertices to 0
		for i in range(no):
			v1[i][0] = 0
			v2[i][0] = 0
	else:
		# X-Z PLANE, Y=0
		# set the y vertice of all vertices to 0
		for i in range(no):
			v1[i][1] = 0
			v2[i][1] = 0

def po():
	global v1,v2,no
	win = GraphWin("PARALLEL-ORTHOGRAPHIC PROJECTION",900,900)
	win.setCoords(-500,-500,500,500)	
	drawAxis(win)

	# take input from input file 
	f = open("project.txt")
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

	# Translation factor
	#pt = f.readline().strip('\n').split(" ")
	#tx,ty,tz = int(pt[0]),int(pt[1]),int(pt[2])
	#ShiftV(v1,tx,ty,tz)
	#ShiftV(v2,tx,ty,tz)

	win = drawFigure(no,v1,v2,win)
	t=Text(Point(v1[0][0],v1[0][1]),"Fig1")
	t.setTextColor('blue')
	t.draw(win)


	Plane()	
	# now v1 and v2 represents parallel orthogonal projections
	#win = drawFigure(no,v1,v2,"green",win)
	win = drawFigure(no,v1,v2,win)
	print("\n\nNOTE: If you cannot see any change, look closely the edge colors must have ")
	print("changed,sometimes happens when trying to show 3D figures\n")
	print("\n*************************************************************")
	print("Mouse Click on the Graphics Window to continue !!!")
	print("*************************************************************\n")
	win.getMouse()
	win.close()

