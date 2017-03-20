n=int(input())

d,f=0,0
for x in range(n):
	r=int(input())
	if r >= 10 and r<= 20:
		d+=1
	else:
		f+=1

print "%d in"  %d
print "%d out" %f