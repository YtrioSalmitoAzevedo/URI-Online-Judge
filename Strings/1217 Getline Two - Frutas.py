n=int(input());p=kg=0;
for x in range(n):
    p+=float(input())
    k=list(map(str, input().split()))
    kg+=len(k)
    print ("day %d:" % (x+1),len(k),"kg")

print ("%.2f" % (kg/n),"kg by day")
print ("R$ %.2f" % (p/n),"by day")
