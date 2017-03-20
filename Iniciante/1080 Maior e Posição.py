a, maior, pos = 0, 0, 0
for x in range(100):
	n=int(input())
	if n>a:
		maior=n
		pos=x+1
	a=maior

print "%d\n%d" %(maior, pos)
