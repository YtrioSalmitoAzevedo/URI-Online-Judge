tc, tr, ts, total = 0, 0, 0, 0
casos = int(input())

for x in range(casos):
	case = raw_input().split(" ")
	if case[1] == "R":
		tr+=int(case[0])
	elif case[1] == "S":
		ts+=int(case[0])
	elif case[1] == "C":
		tc+=int(case[0])
	total+=int(case[0])

total=float(total)
t1=((tc*100)/total)
t2=((tr*100)/total)
t3=((ts*100)/total)

print "Total: %d cobaias" %total
print "Total de coelhos: %d" %tc
print "Total de ratos: %d" %tr
print "Total de sapos: %d" %ts
print "Percentual de coelhos: %0.2f %%" %t1
print "Percentual de ratos: %0.2f %%" %t2
print "Percentual de sapos: %0.2f %%" %t3
