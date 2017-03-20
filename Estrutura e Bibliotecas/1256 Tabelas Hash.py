def hash(l, mat):
	a, dic=[], {}
	for i in range(l[0]):
		lis=[]
		for j in range(l[1]):
			if mat[j] % l[0] == i:
				lis.append(mat[j])
		if lis != []:
			a.append(lis)
			x=str(lis)
			for h in ["[","]"]:
				x=x.replace(h, "")
			x=x.replace(", "," -> ")
			print i, "->", x,"->","\\"
		else:
			print i,"->","\\" 
f=0
n=int(input())
for x in range(n):
	if f == 1:
		print 
	a, b    = map(int ,raw_input().split())
	matrix  = map(int, raw_input().split())
	hash([a, b], matrix)
	f=1