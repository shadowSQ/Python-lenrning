import math

def eryuanyici(a,b,c):
	x1 = -b + math.sqrt(b*b-4*a*c)
	x2 = -b - math.sqrt(b*b-4*a*c)
	return x1,x2
	
	