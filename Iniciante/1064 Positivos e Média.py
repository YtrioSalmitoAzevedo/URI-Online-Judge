a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

list=[a, b, c, d, e, f]

count, media = 0, 0
for x in list:
	if x > 0:
		media+=x
		count+=1

media=media/count
print "%d valores positivos" %count
print "%0.1f" %media