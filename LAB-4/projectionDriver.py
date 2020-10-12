""" PLEASE COMPILE WITH : sudo python3 transform2d.py  """

"""YUKTI KHURANA - 2017UCP1234, A4"""


import arbitraryParallel
import parallelOrtho
import ObliqueParallel
import Axonometric
import perspective


def printIntro():
	print("\n*************************************************************")
	print("\nWELCOME TO PROJECTIONS BY YUKTI\n")
	print("PRESS o+Enter for PARALLEL ORTHOGRAPHIC PROJECTION  !")
	print("PRESS a+Enter for ARBITRARY PLANE PARALLEL ORTHOGRAPHIC PROJECTION !")
	print("PRESS c+Enter for OBLIQUE PARALLEL PROJECTION (Cabinet/Cavalier)!")
	print("PRESS x+Enter for AXONOMETRIC PROJECTION(Isometric,Dimetric,Trimetric) !")
	print("PRESS p+Enter for PERSPECTIVE PROJECTION (& Vanishing Points)!")
	print("PRESS e+Enter to EXIT !")
	print("***************************************************************\n")
	

def main():	
	while True:	
		printIntro()
		choice = input("Enter your choice : ")	
		if (choice == "o"):
			parallelOrtho.po();
		elif (choice == "a"):
			arbitraryParallel.ap();
		elif (choice == "c"):
			ObliqueParallel.op();
		elif (choice == "x"):
			Axonometric.ax()
		elif (choice == "p"):
			perspective.p();
		elif (choice == "e"):
			print("Thank you. Bye")
			print("Yukti Khurana 2017UCP1234")
			exit()
		else:
			print("Sorry! Wrong Option...Try again")
	
main()


"""YUKTI KHURANA - 2017UCP1234, A4"""
