def tFood(n):
	dias=0
	while n>1:
		n=n/2
		dias+=1
	return dias

n=int(input())
for x in range(n):
	k=float(input())
	print `tFood(k)`+" dias"