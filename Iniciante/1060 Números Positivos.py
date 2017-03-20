a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

list=[a, b, c, d, e, f]

count = 0
for x in list:
	if x > 0:
		count+=1

print "%d valores positivos" %count