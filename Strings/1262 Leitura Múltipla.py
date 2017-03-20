def multRW(st, ps):
	LR, LW, summ = [], [], 0
	for x in st:
		if x == 'W':
			LW.append(x)
		else:
			LR.append(x)
	summ=len(LW)
	summ+=len(LR)/ps 
	return summ

while True:
	try:
		st = raw_input()
		ps = int(input())
		print "{0}".format(multRW(st, ps))
	except:
		break