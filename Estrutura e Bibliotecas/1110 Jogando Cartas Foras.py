def discardCard(n):
    L=[];rm=[]
    for x in range(1, n+1):
        L.append(x)

    while len(L) != 1:
        rm.append(L.pop(0))
        L.append(L.pop(0))

    print "Discarded cards:", ', '.join(str(y) for y in rm)
    print "Remaining card:", L[0]


n=int(raw_input())
while n != 0:
    discardCard(n)
    n=int(raw_input())