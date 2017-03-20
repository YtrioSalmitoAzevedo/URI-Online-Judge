from math import sqrt
numbers = raw_input().split(" ")
a, b, c = numbers
a, b, c = float(a), float(b), float(c)
delta = b*b - 4*a*c
if delta < 0 or a == 0:
	print "Impossivel calcular"
else:
	r1 = ((-b + sqrt(delta))/(2*a))
	print "R1 = %0.5f" %r1 
	r2 = ((-b - sqrt(delta))/(2*a))
	print "R2 = %0.5f" %r2