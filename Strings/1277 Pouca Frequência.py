def pfreq(a, b, c):
	dic,leng, conc, blank={},len(c), "", 0
	for x in range(leng):
		if len(c[x].replace("M", "")) != 0:   
			c[x]=c[x].replace("M", "")
		tp=len(c[x].replace("A", "P"))
		dp=len(c[x].replace("A", ""))
		dic[b[x]]=((dp*100)/tp)
		if dic[b[x]] < 75:
			conc  += ((" "*blank)+b[x])
			blank = 1
	print "%s" %conc

n=int(input())
for x in range(n):
	a=int(input()) 
	b=raw_input().split()
	c=raw_input().split()
	pfreq(a, b, c)
