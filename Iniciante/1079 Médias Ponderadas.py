loops = int(input())
resultado = []
for x in range(loops):
	numbers=raw_input().split()
	a, b, c = numbers
	a, b, c = float(a),float(b),float(c)
	r = (a*2+b*3+c*5)/10
	resultado.append(r)

for y in resultado:
	print "%0.1f" %y
