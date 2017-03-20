def order(x,li):
    for k in range(len(li)):
        if x==li[k]:
            return k
def char(n,li):
    for k in range(len(li)):
        if n == k:
            return li[k]

def cifra(a, b):

     L=[]
     for jj in range(26):
        L.append(chr(ord('A')+jj))

     for f in range(len(a)):
        a[f]=char( ( order(a[f], L) - b ) % 26, L)

     return "".join(a)

for x in range(input()):
    print cifra(list(raw_input()), input())