# ODD NEGATIVE
# NULL
# ODD POSITIVE
# EVEN NEGATIVE

n=int(input())
numbers=[]
for x in range(n):
	number=int(input())
	numbers.append(number)


for y in range(len(numbers)):
	if numbers[y] == 0:
		print "NULL"
	if numbers[y] < 0 and numbers[y] % 2 == 0:
		print "EVEN NEGATIVE"
	if numbers[y] > 0 and numbers[y] % 2 == 0:
		print "EVEN POSITIVE"
	if numbers[y] > 0 and numbers[y] % 2 != 0:
		print "ODD POSITIVE"
	if numbers[y] < 0 and numbers[y] % 2 != 0:
		print "ODD NEGATIVE"