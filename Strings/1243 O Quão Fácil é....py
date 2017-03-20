# -*- coding: utf-8 -*-
def isAlpha(x):
    if x>='a' and x<='z' or x>='A' and x<='Z':
        return True
    return False


def noWord(L, x):
    word=L[x];p=''; c=0
    for j in range(len(word)):
        if isAlpha(word[j]):
            c=c+1
            if (len(word)-c) == 1:
                if j+1 < len(word):
                    if word[j+1] == '.':
                        p=word[j+1]
    if c==len(word) or p=='.':
        return c
    else:
        return -1

def howEasy( str ):
    s=0
    div=len(str)
    soma=0
    for k in range(len(str)):
        soma=noWord(str, k)
        if soma != -1:
            s+=soma
        else:
            div=div-1
    if div == 0:
        m=0
    else:
        m=(s/div)

    if m <= 3:
        print 250
    elif m==4 or m==5:
        print 500
    else:
        print 1000

while True:
    try:
        howEasy(raw_input().split())
    except:
        break

