listaInteiros=raw_input().split(" ")
a, b, c   = listaInteiros
(a, b, c) = (int(a), int(b), int(c))

maiorAB=(a+b+(abs(a-b)))/2

if c > maiorAB:
   maiorAB=c

print("%d eh o maior" %maiorAB)
