multiplos = raw_input().split(" ")
a, b = multiplos
a, b = int(a),int(b)

if a > b:
	mm,m=a,b
else:
	mm,m=b,a

if mm % m == 0:
	print "Sao Multiplos"
else:
	print "Nao sao Multiplos"
