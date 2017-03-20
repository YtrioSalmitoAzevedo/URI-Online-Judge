def searchMax(lista, number):
	for x in range(len(lista)):
		if number==len(lista[x]):
			return x

def ordLen(w):
	numbers, el=[], []
	for i in range(len(w)):
		numbers.append(len(w[i]))
	numbers.sort(reverse=True)

	for j in numbers:
		pos=searchMax(w, j)
		el.append(w[pos])

	return " ".join(el)

for x in range(int(input())):
	words=raw_input().split()
	print "%s" %ordLen(words)