from graphics import *
from graphicLibClass import *
from polygon1 import *
import math

xMin = 0
xMax = 0
yMin = 0
yMax = 0

edgeTable = {}
vertex = []
activeTable = []


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
    			c = transformX(math.ceil(x1))
    			d = transformX(math.floor(x2))
    			k = transformY(i)
    			line(c,k,d,k,win,color)
    			
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

    
def main():

    win = GraphWin("Scan Line Polygon Filling algorithm",900,900)
    win.setCoords(-450,-450,450,450)		
    win = drawAxis(win)
    n = int(input("Enter the no of vertices of the quadrilateral : "))
    print("Enter the points in cyclic manner : ")

    for i in range(n):
        x = int(input("Enter the x coordinate of the point : "))
        y = int(input("Enter the y coordinate of the point : "))
        if(i==0):
            x0,y0 = x,y
        vertex.append((x,y))
    vertex.append((x0,y0))
    
    b_color  = input("Enter the boundary color of polygon = ")
    win = drawPolygon(n,vertex,win,b_color)
    print("\nVERTEX TABLE : ")
    print(vertex,"\n")
    color = input("Enter the color you want to fill in the polygon = ")
    win = ScanLineFilling(n,vertex,color,win)

    win.getMouse()
    win.close()
main()
