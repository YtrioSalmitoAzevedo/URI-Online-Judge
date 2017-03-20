def encaixa(a, b):
	ca, cb, cout  = str(a), str(b), 0
	dif = len(ca) - len(cb)
	fat = ca[dif:len(ca)]
	fat = str(fat) 
	for x in range(len(fat)):
		if fat[x] == cb[x]:
			cout += 1
	if cout == len(fat):
		return "encaixa"
	else:
		return "nao encaixa"

n=int(input())
for x in range(n):
	a, b = map(int, raw_input().split())
	print "%s" %encaixa(a, b)