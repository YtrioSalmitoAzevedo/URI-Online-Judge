a, b   = int(input()),int(input()) 
c, d, e =int(input()),int(input()),int(input())

lista = [a, b, c, d, e]
pares=0
for x in lista:
	if x % 2 == 0:
		pares+=1

print "%d valores pares" %pares
