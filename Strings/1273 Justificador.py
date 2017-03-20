def justy(l):
	m=max(map(len, l))
	for x in l:
		if len(x) != m:
			marginL = (m - len(x))
			print "%s%s" %(marginL*" ", x)
		else:
			print "%s" %x

flag = 0
while True:
	n,L=int(input()), []
	if n == 0:
		break
	if flag == 1: 
		print;
	for x in range(n):
		L.append(raw_input())
	justy(L)
	flag = 1
