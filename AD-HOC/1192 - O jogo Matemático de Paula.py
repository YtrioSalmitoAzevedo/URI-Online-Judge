# -*- coding: utf-8 -*-

L = [];n = int(input())
for x in range(n):
    k = raw_input()
    L.append(k)

def f(L):
    for x in L:
        c = x
        if int(c[0]) == int(c[2]):
               print(int(c[0]) * int(c[2]))
        elif c[1] == c[1].upper():
               print(int(c[2]) - int(c[0]))
        else:
               print(int(c[0]) + int(c[2]))

f(L)
