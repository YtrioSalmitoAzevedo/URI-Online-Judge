floats  = raw_input().split(" ")
A, B, C = floats
A, B, C = float(A), float(B), float(C)

if A < B:
	t = A
	A = B
	B = t
if A < C:
	t = A
	A = C
	C = t
if B < C:
	t = B
	B = C
	C = t

if A >= B+C:
	print "NAO FORMA TRIANGULO"
else:
	if A**2 == B**2 + C**2:
		print "TRIANGULO RETANGULO"
	if A**2 > B**2 + C**2:
		print "TRIANGULO OBTUSANGULO"
	if A**2 < B**2 + C**2:
		print "TRIANGULO ACUTANGULO"
	if A==B and A==C and B==C:
		print "TRIANGULO EQUILATERO"
	else:
		if A==B or A==C or B==C:
			print "TRIANGULO ISOSCELES"