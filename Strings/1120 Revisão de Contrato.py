def contrato(b, n):
	bs, snumber, r, c = str(b), list(str(n)), 0, 0
	for i, v in enumerate(snumber):
		if bs == v:
			snumber[i]=v.replace(bs, "")
			c+=1
	if c == len(snumber):
		return 0
	return int("".join(snumber))

b, n = 1, 1
while b != 0 and n != 0: 
	b, n = map(int, raw_input().split())
	if b != 0 and n != 0:
		print "%d" %contrato(b, n)
