numbers = raw_input().split()
x, y, z = numbers
x, y, z = (int(x), int(y), int(z))

if x < y and y < z:
	(a, b, c)=(x, y, z)
elif x < z and z < y:
	(a, b, c)=(x, z, y)
elif y < x and x < z:
	(a, b, c)=(y, x, z)
elif y<z and z<x:
	(a, b, c)=(y, z, x)
elif z<x and x<y:
	(a, b, c)=(z, x, y)
elif z<y and y<x:
	(a, b, c)=(z, y, x)

print ("%d\n%d\n%d\n" %(a, b, c))
print ("%d\n%d\n%d"   %(x, y, z))
