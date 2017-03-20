def acimaDaMedia(ls):
	soma,count=0,0
	for i in range(1, len(ls)):
		soma += int(ls[i])
	media = soma/float(ls[0])
	for j in range(1, len(ls)):
		if int(ls[j]) > media:
		   count+=1
	return ((count*100)/float((ls[0])))

n=int(input())
for x in range(n):
	l=raw_input().split(" ")
	print "%0.3f%%" %acimaDaMedia(l)
