# -*- coding: utf-8 -*-

def isAlpha(x):
    if x>='a' and x<='z' or x>='A' and x<='Z':
        return True
    return False

def firstLetter(L):
    for j in range(len(L)):
        if isAlpha(L[j]) is True:
            return j
    return -1


def sentDan( str ):

    count=1;copy=list(str)
    f=firstLetter(copy)
    copy[f]=copy[f].upper()

    for k in range(f+1, len(copy)):
        if isAlpha(copy[k]) == True:
            if count % 2 == 0:
                copy[k]=copy[k].upper()
            else:
                copy[k]=copy[k].lower()
            count=count+1

    return "".join(copy)

while True:
    try:
        print sentDan(raw_input())
    except:
        break
