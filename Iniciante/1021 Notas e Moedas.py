valor=float(input())
a=["100.00", "50.00", "20.00", "10.00", "5.00", "2.00"]
b=["1.00", "0.50", "0.25", "0.10", "0.05" ,"0.01"]
print("NOTAS:")
for x in a:
    print("%d nota(s) de R$ %s" %(valor/float(x), x))
    valor=valor % float(x)

print("MOEDAS:")
for y in b:
    print("%d moedas(s) de R$ %s" %(valor/float(y), y))
    valor=valor % float(y)