nota=int(input())
cedulas=[100, 50, 20, 10, 5, 2,1]
print("%d" %nota)
for x in cedulas:
    print("%d nota(s) de R$ %d,00" %(nota/x, x))
    nota=nota % x
