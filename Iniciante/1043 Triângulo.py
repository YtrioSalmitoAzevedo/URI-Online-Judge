sides = raw_input().split(" ")
a, b, c = sides
a, b, c = (float(a), float(b), float(c))

c1=abs(b - c) < a < b + c
c2=abs(a - c) < b < a + c
c3=abs(a - b) < c < a + b

if c1 and c2 and c3:
	print ("Perimetro = %0.1f"%(a+b+c))
else:
	print ("Area = %0.1f"%((a+b)*c/2))


