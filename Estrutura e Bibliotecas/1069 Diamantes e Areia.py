def diamente(str):
	contagem=0
	str=list(str.replace(".",""))
	a, b = "<",">"
	while True:
		for x, v in enumerate(str):
			if x+1 < len(str):
				if str[x] == a and str[x+1] == b:
					contagem+=1
					for i in [x, x+1]:
						str[i]=''
		str=list("".join(str))
		if "".join(str).count("<>") == 0:
				return contagem
n=int(input())
for x in range(n):
	string=raw_input()
	print "%d" %diamente(string)