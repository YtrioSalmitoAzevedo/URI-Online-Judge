A = raw_input().split(" ")
B = raw_input().split(" ")
c1, qtd1, v1 = A
c2, qtd2, v2 = B

total=( (int(qtd1)*float(v1)) + (int(qtd2)*float(v2)) )
print("VALOR A PAGAR: R$ %0.2f" %total)
