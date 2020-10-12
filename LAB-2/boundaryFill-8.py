from graphics import *
# for constructing a polygon to fill color in
from polygon import *

stack = []
already_filled = []


def putpixel(x,y,color,win):
	p = Point(x,y)
	p.draw(win)
	p.setFill(color)

# non-recursive flood fill using a stack
def boundaryFillAlgo8(x,y,color,win):
	stack.append((x,y))
	while(len(stack)!= 0):
		x,y = stack.pop()
		if ((x,y) not in boundary_values and (x,y) not in already_filled):
			putpixel(x,y,color,win)
			already_filled.append((x,y))
			
		if ((x+1,y) not in boundary_values and (x+1,y) not in already_filled):
			stack.append((x+1,y))
			
		if ((x,y+1) not in boundary_values and (x,y+1) not in already_filled):
			stack.append((x,y+1))
			
		if ((x-1,y) not in boundary_values and (x-1,y) not in already_filled):
			stack.append((x-1,y))
			
		if ((x,y-1) not in boundary_values and (x,y-1) not in already_filled):
			stack.append((x,y-1))	
		
		if ((x+1,y+1) not in boundary_values and (x+1,y+1) not in already_filled):
			stack.append((x+1,y+1))
			
		if ((x+1,y-1) not in boundary_values and (x+1,y-1) not in already_filled):
			stack.append((x+1,y-1))
			
		if ((x-1,y-1) not in boundary_values and (x-1,y-1) not in already_filled):
			stack.append((x-1,y-1))
			
		if ((x-1,y+1) not in boundary_values and (x-1,y+1) not in already_filled):
			stack.append((x-1,y+1))	
				
	return win

def main():
	win = GraphWin("Boundary Fill algorithm",xvmax-xvmin,yvmax-yvmin)
	win.setCoords(xvmin,yvmin,xvmax,yvmax)
	drawAxis(win)		
	n = int(input("Enter the no of points in polygon: "))
	Points=[]
	print("Please enter the coordinates of polygon in a cyclic manner : ")
	for i in range(n):
		print("Enter Point ",i+1,": ")
		x = int(input("x-coordinate: "))
		y = int(input("y-coordinate: "))
		boundary_values.append((x,y))
		Points.append((x,y))
	Points.append((Points[0][0],Points[0][1]))			
	b_color  = input("Enter the boundary color of polygon = ")
	drawPolygon(n,Points,win,b_color)	
	
	color = input("Enter the color you want to fill in the polygon = ")
	print("Enter the coordinate where to start filling from : ")
	x = int(input("x-coordinate : "))
	y = int(input("y-coordinate : "))
	if ((x,y) in boundary_values):
		print("The coordinate should not be a boundary value!")
		exit()
	
	boundaryFillAlgo8(x,y,color,win)
	
	win.getMouse()
	win.close()

main()
