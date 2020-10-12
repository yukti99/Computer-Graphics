from graphics import *
from lib import *


# region codes 
INSIDE = 0  #0000 
LEFT = 1    #0001 
RIGHT = 2   #0010 
BOTTOM = 4  #0100 
TOP = 8     #1000 
xmax = 0.0
ymax = 0.0
xmin = 0.0
ymin = 0.0



def Code(x,y): 
    code = INSIDE 
    # setting bits according to region wrt to rectangle
    if x < xmin:      
        code |= LEFT 
    elif x > xmax:    
        code |= RIGHT 
    if y < ymin:     
        code |= BOTTOM 
    elif y > ymax:   
        code |= TOP   
    return code 
    
def cohenClipping(x1,y1,x2,y2,win):

	x11 = x1
	y11 = y1
	x22 = x2
	y22 = y2
	# region codes for both points of the line
	code1 = Code(x1,y1)
	code2 = Code(x2,y2)
	accept = False
	while(True):
		# trivially accepted
		if code1 == 0 and code2 == 0:
		    accept = True
		    break
		# trivially rejected
		elif (code1 & code2 )!=0:
			break
			
		# line needs to be clipped
		else:
			x = 1.0
			y = 1.0			
			# select the code outside the given rectangle
			if (code1 != 0):
				out_code = code1
			else:
				out_code = code2

			if (out_code & TOP): # Find intersection point 
				x = x1 + ( (x2-x1)*(ymax-y1) ) /(y2-y1) # y = y1 + slope * (x - x1)  
				y = ymax
			if (out_code & BOTTOM): # Find intersection point 
				x = x1 + ( (x2-x1)*(ymin-y1) ) /(y2-y1) # y = y1 + slope * (x - x1)  
				y = ymin
			elif (out_code & RIGHT):
				y = y1 + ( (y2-y1)*(xmax-x1) ) /(x2-x1) 
				x = xmax
			elif (out_code & LEFT):
				y = y1 + ( (y2-y1)*(xmin-x1) ) /(x2-x1) 
				x = xmin
			if (out_code == code1):
				x1,y1 = x,y
				code1 = Code(x1,y1)
			else:
				x2,y2 = x,y
				code2 = Code(x2,y2)
	if (accept):
		x1 = int(x1)
		x2 = int(x2)
		y1 = int(y1)
		y2 = int(y2)
		#l1 = Text(Point(x1,y1),'('+str(x1)+ ','+str(y1)+ ')')
		#l2 = Text(Point(x2,y2),'('+ str(x2)+ ','+str(y2)+ ')')
		#l1.draw(win)
		#l2.draw(win)
		print("Line is accepted from (%.2f,%.2f) to (%.2f,%.2f)" % (x1,y1,x2,y2))
		win.getMouse()
		win = line(int(x2),int(y2),int(x22),int(y22),win,"red")
		win = line(int(x11),int(y11),int(x1),int(y1),win,"red")
	else: 
		print("Line is rejected")  
	return win
           

def main():
	global xmin,xmax,ymin,ymax
	win = GraphWin("COHEN SUTHERLAND CLIPPING ALGORITHM",900,900)
	win.setCoords(-450,-450,450,450)	
	win = drawAxis(win)
	print("Enter the rectangular region : ")
	xmin = int(input("Enter the min x-coordinate = "))
	xmax = int(input("Enter the max x-coordinate = "))
	ymin = int(input("Enter the min y-coordinate = "))
	ymax = int(input("Enter the max y-coordinate = "))	
	
	Points = [(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax),(xmin,ymin)]
	l1 = Text(Point(xmin,ymin),'('+str(xmin)+ ','+str(ymin)+ ')')
	l2 = Text(Point(xmax,ymin),'('+ str(xmax)+ ','+str(ymin)+ ')')
	l3 = Text(Point(xmax,ymax),'('+str(xmax)+ ','+str(ymax)+ ')')
	l4 = Text(Point(xmin,ymax),'('+ str(xmin)+ ','+str(ymax)+ ')')
	l1.draw(win)
	l2.draw(win)
	l3.draw(win)
	l4.draw(win)
	
	win = drawPolygon(4,Points,win,"green")
	
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
	
	win = line(x1,y1,x2,y2,win,"blue")
	
	win = cohenClipping(x1,y1,x2,y2,win)
	win.getMouse()
	win.close()

main()