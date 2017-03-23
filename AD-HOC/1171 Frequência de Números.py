# -*- coding: utf-8 -*-
L = []
n = int(input())
for x in range(n):
    k = int(input())
    L.append(k)

def f(L):
    c = [];m=sorted(list(set(L)))
    for n in range(len(m)):
        t = m[n] # Elemento atual
        c.append(0) # Inicializa o contador
        for k in L:
            if k == t:
                c[n]+=1
    for x in range(len(m)):
        print m[x], "aparece", c[x], "vez(es)"
f(L)
