def helloGalaxy(L):
	M=[]
	for j in L:
		M.append(int(j[1])-int(j[2]))
	v=min(M)
	for x in range(len(M)):
		if v==M[x]:
			print "%s" %L[x][0]
			break
while True:
	n=int(input())
	if n==0:
		break
	L=[]
	for x in range(n):
		L.append(raw_input().split())
	helloGalaxy(L)
