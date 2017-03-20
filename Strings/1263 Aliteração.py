def alli(words):
	
	count,con=[],0
	for x in range(len(words)):
		count.append(words[x][0].lower())
	cs, dic=set(count), {}

	for x in cs:
		dic[x]=0

	for j in range(len(words)):
		if j+1 < len(words): 
			a, b = words[j][0].lower(), words[j+1][0].lower()
			if a == b:
				if con == 0:
					dic[a] +=1
				con=1
			else:
				con=0
	
	print "%d" %sum(dic.values())

while True:
	try:
		alli(raw_input().split())
	except:
		break