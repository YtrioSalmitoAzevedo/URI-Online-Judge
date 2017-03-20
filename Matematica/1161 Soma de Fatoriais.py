def fat(n):
	if n<=0:
		return 1
	return n*fat(n-1)

while True:
	try:
		n=map(int, raw_input().split())
		print (fat(n[0])+fat(n[1])) 
	except:
		break	