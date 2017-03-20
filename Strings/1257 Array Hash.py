def pAlpha(c):
		return map(chr, 
			  range(65, 91)).index(c.upper())
def cHash(l):
	value=0
	for c in range(len(l)):
		el=l[c]
		for j in range(len(el)):
			value+=(pAlpha(el[j])+c+j)
	return value

i=int(input())
for x in range(i):
	j,l=int(input()),[]
	for y in range(j):
		l.append(raw_input())
	print "%d" %cHash(l)
		