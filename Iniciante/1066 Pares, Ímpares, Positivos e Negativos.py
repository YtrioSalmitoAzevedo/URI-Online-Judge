cp, ci, cpp, neg = 0, 0, 0, 0
a, b   = int(input()),int(input()) 
c, d, e =int(input()),int(input()),int(input())

lista=[a, b, c, d, e]
for x in lista:
	if x % 2 == 0:
		cp+=1
	else:
		ci+=1
	
	if x > 0:
		cpp+=1
	elif x < 0:
		neg+=1

print "%d valor(es) par(es)"     %cp
print "%d valor(es) impar(es)"   %ci
print "%d valor(es) positivo(s)" %cpp
print "%d valor(es) negativo(s)" %neg