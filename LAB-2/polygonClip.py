from graphics import *
from lib import *
import time
import math

edgeTable = {}
vertex = []
activeTable = []
origin = [0, 0]
refvec = [0, 1]

def ScanLineFilling(n,vertex,color,win):
	ymin = vertex[0][1]
	ymax = vertex[0][1]
	print("ymin = ",ymin)
	print("ymax = ",ymax)
	
	# initial x and y
	xi = vertex[0][0]
	yi = vertex[0][1]
	print("vertex table = ",vertex)
	# creation of edge table -  will not contain horizontal edges
	for i in range(1,n+1):
	
		y1 = vertex[i-1][1]
		x1 = vertex[i-1][0]
		
		y = vertex[i][1]
		x = vertex[i][0]
		ymin = min(ymin,y)
		ymax = max(ymax,y)
		# we have to ignore horizontal lines
		if (y1 != y):
			if (x1 != x):
				m = (y-y1)/(x-x1)
			else:
				# slope is infinity i.e vertical line
				m = 10**9
			if min(y1,y) not in edgeTable:
				edgeTable[min(y1,y)]=[]
			if y1<y:
				edgeTable[min(y1,y)].append([x1,max(y1,y),1/m])

			else:
				edgeTable[min(y1,y)].append([x,max(y1,y),1/m])
	print(ymax,ymin)
	# filling starts from bottom to up so y is incremented by 1
	print("edge table = ",edgeTable)
	for i in range(ymin,ymax):
    		if i in edgeTable:
    			for j in edgeTable[i]:
    				activeTable.append(j)
    		
    		activeTable.sort()
    		#print(activeTable)
    		a = 0
    		b = 1
    		while b<len(activeTable):
    			x1 = activeTable[a][0]
    			x2 = activeTable[b][0]
    			c = (math.ceil(x1))
    			d = (math.floor(x2))
    			#k = transformY(i)
    			l = Line(Point(c,i),Point(d,i))
    			l.setFill(color)
    			l.draw(win)
    			#line(c,k,d,k,win,color)
    			
    			if(activeTable[b][1]==i+1):
    			       	activeTable.pop(b)
    			else:
    				activeTable[b][0]+=activeTable[b][2]
    			if (activeTable[a][1]==i+1):
    				activeTable.pop(a)
    			else:
    				activeTable[a][0]+=activeTable[a][2]
    			a+=2
    			b+=2
    	
	return win 
    
def intersect_x(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
	return num//den
def intersect_y(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
	return num//den
	
	
def util(polygon,clipWindow,x1,y1,x2,y2):
	new_points = []
	n = len(polygon)
	for i in range(n):
		k = (i+1)%n
		kx,ky = polygon[k][0],polygon[k][1]
		ix,iy = polygon[i][0],polygon[i][1]
		i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)
		k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)
		if(i_pos<0 and k_pos<0):
			new_points.append([kx,ky])
		elif(i_pos>=0 and k_pos<0):
			tempx = intersect_x(x1,y1,x2,y2,ix,iy,kx,ky)
			tempy = intersect_y(x1,y1,x2,y2,ix,iy,kx,ky)
			new_points.append([tempx,tempy])
			new_points.append([kx,ky])
		elif(i_pos<0 and k_pos>=0):
			tempx = intersect_x(x1,y1,x2,y2,ix,iy,kx,ky)
			tempy = intersect_y(x1,y1,x2,y2,ix,iy,kx,ky)
			new_points.append([tempx,tempy])

	print(new_points)
	return new_points

def Polygonclip(polygon,clipWindow):

	n = len(clipWindow)
	for i in range(n):
		k = (i+1)%n
		polygon = util(polygon,clipWindow,clipWindow[i][0],clipWindow[i][1],clipWindow[k][0],clipWindow[k][1])
	return polygon

def main():
	global xmin,xmax,ymin,ymax,clipWindow,sides
	win = GraphWin("POLYGON LINE CLIPPING ALGORITHM",900,900)
	win.setCoords(-450,-450,450,450)	
	win = drawAxis(win)
	
	sides=int(input("Enter number of sides of polygon = "))
	s=[]
	temp=[]

	for i in range(sides):
		x = int(input("Enter x : "))
		y = int(input("Enter y : "))
		s.append((x,y))

	# drawing the polygon
	for i in range(sides-1):
		p1 = Point(s[i][0],s[i][1])
		p2 = Point(s[i+1][0],s[i+1][1])
		l = Line(p1,p2)
		l.draw(win)
	p1 = Point(s[0][0],s[0][1])
	p2 = Point(s[sides-1][0],s[sides-1][1])
	l = Line(p1,p2)
	l.draw(win)

	print("Enter the clipping rectangular region : ")
	c=[]
	for i in range(4):
		x = int(input("Enter x : "))
		y = int(input("Enter y : "))
		c.append((x,y))

	# drawing the clipping window
	for i in range(3):
		p1 = Point(c[i][0],c[i][1])
		p2 = Point(c[i+1][0],c[i+1][1])
		l = Line(p1,p2)
		l.draw(win)
	p1 = Point(c[0][0],c[0][1])
	p2 = Point(c[sides-1][0],c[sides-1][1])
	l = Line(p1,p2)
	l.draw(win)


	list1 = Polygonclip(s,c)
	m = len(list1)
	print("list = ",list1)
	win = ScanLineFilling(len(list1)-1,list1,"green",win)
	for i in range(m):
		k = (i+1)%m
		p1 = Point(list1[i][0],list1[i][1])
		p2 = Point(list1[k][0],list1[k][1])
		line = Line(p1,p2)
		line.setFill("green")
		line.draw(win)
	
	win.getMouse()
	win.close()

main()