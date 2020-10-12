from graphics import *


xwmin = 0
xwmax = 0
xvmin = 0
xvmax = 0
ywmin = 0
ywmax = 0
yvmin = 0
yvmax = 0


def transformX(xw):
	t = (xvmax-xvmin)/(xwmax-xwmin)
	xv = xvmin + ((xw-xwmin)*t)
	return int(xv)
	
def transformY(yw):
	t = (yvmax-yvmin)/(ywmax-ywmin)
	yv = yvmin + ((yw-ywmin)*t)
	return int(yv)

def drawEllipse(rx, ry, xc, yc,win): 
    xc = transformX(xc) 
    yc = transformX(yc) 
    print("The viewport coordinates of centre : ","(",xc,",",yc,")")

    x = 0;  
    y = ry;
    
    # Decision variable of region 1  
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx));  
    dx = 2 * ry * ry * x;  
    dy = 2 * rx * rx * y;  
  
    # region-1  
    while (dx < dy):
    	p1 = Point(transformX(x+xc),transformY(y+yc))
    	p1.draw(win)
    	p1.setFill('purple')
    	p2 = Point(transformX(-x+xc),transformY(y+yc))
    	p2.draw(win)
    	p2.setFill('purple')
    	p3 = Point(transformX(x+xc),transformY(-y+yc))
    	p3.draw(win)
    	p3.setFill('purple')
    	p4 = Point(transformX(-x+xc),transformY(-y+yc))
    	p4.draw(win)
    	p4.setFill('purple') 
    	time.sleep(0.003) 
    	if (d1 < 0):
    		x+=1
    		dx+=(2*ry*ry)
    		d1+=dx+(ry*ry)
    	
    	else:
    		x+=1
    		y-=1
    		dx+=(2*ry*ry)
    		dy-=(2*rx*rx)
    		d1+=dx-dy+(ry*ry)
   
    # Decision variable for region 2  
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +((rx * rx) * ((y - 1) * (y - 1)))-(rx * rx * ry * ry));  
  
    # region-2
    while (y >= 0):
    	p1 = Point(transformX(x+xc),transformY(y+yc))
    	p1.draw(win)
    	p1.setFill('purple')
    	p2 = Point(transformX(-x+xc),transformY(y+yc))
    	p2.draw(win)
    	p2.setFill('purple')
    	p3 = Point(transformX(x+xc),transformY(-y+yc))
    	p3.draw(win)
    	p3.setFill('purple')
    	p4 = Point(transformX(-x+xc),transformY(-y+yc))
    	p4.draw(win)
    	p4.setFill('purple')
    	time.sleep(0.003)
    	if (d2>0):
    		y-=1
    		dy-=(2*rx*rx)
    		d2+=(rx*rx)-dy
    	else:
    		y-=1
    		x+=1
    		dx+=(2*rx*ry)
    		dy-=(2*rx*rx)
    		d2+=dx-dy+(rx*rx)
    	
         
		

def main():
	# default boundary values for window and viewport
	global xwmin,xwmax,xvmin,xvmax,ywmin,ywmax,yvmin,yvmax	
	xvmin = -450
	yvmin = -450
	xvmax = 450	
	yvmax = 450
	xwmin = -2000
	ywmin = -2000
	xwmax = 2000	
	ywmax = 2000
	print("Enter the coordinates of center of the Ellipse : ")	
	cx = int(input("x-coordinate: "))
	cy = int(input("y-coordinate: "))
	rmajor = int(input("Enter the radius of major of ellipse: "));
	rminor = int(input("Enter the radius of minor of ellipse: "));	
	'''print("Enter the boundary values for window :")
	xwmin = int(input("min x-coordinate :"))
	xwmax = int(input("max x-coordinate :"))
	ywmin = int(input("min y-coordinate :"))
	ywmax = int(input("max y-coordinate :"))
	print("Enter the boundary values for viewport :")
	xvmin = int(input("min x-coordinate :"))
	xvmax = int(input("max x-coordinate :"))
	yvmin = int(input("min y-coordinate :"))
	yvmax = int(input("max y-coordinate :"))'''			
	win = GraphWin("Ellipse",xvmax-xvmin,yvmax-yvmin)
	win.setBackground("light blue")
	win.setCoords(xvmin,yvmin,xvmax,yvmax)
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
	
	
	
	drawEllipse(rmajor,rminor,cx,cy,win)
	
	win.getMouse()
	win.close()

main()
    #m = Text(Point(xc,yc), "(%d,%d)"%(xc,yc))
    #m.setTextColor("purple")
    #m.setSize(10)
    #m.draw(win)
    #p = Point(xc,yc)
    #p.setFill('purple') 
    #p.draw(win)
    #m = Text(Point(cx,cy), "(%d,%d)"%(cx,cy))
    #m.setTextColor("red")
    #m.setSize(10)
    #m.draw(win)
    #p = Point(cx,cy) 
    #p.setFill('red') 
    #p.draw(win)

