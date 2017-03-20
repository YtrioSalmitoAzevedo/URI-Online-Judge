fin = int(input())
ini = int(input())

if ini > fin:
	t=fin
	fin=ini
	ini=t
c=0
for x in range(ini+1, fin):
	if x % 2 != 0:
		c+=x

print "%d" %c