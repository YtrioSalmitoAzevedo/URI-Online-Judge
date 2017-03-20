def mdc(a, b):
	r=1
	while r!=0:
		c=b
		r=a%b
		a=b
		b=r
	return c

n=int(input())
for x in range(n):
	numbers=map(int, raw_input().split())
	print mdc(numbers[0], numbers[1])