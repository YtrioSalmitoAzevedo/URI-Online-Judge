def paresEimpas(pares, impas):
	 p, i = sorted(pares), sorted(impas, reverse=True)
	 pi   = p + i
	 for n in pi:
	 	print n

n=int(input())
pares, impas = [], []
for x in range(n):
	number=int(input())
	if number % 2 == 0:
		pares.append(number)
	else:
		impas.append(number)
paresEimpas(pares, impas)