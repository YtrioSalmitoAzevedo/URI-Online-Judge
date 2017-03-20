def bubbleSort(v):
    for i in range(len(v)-1, 0, -1):
        for j in range(i):
            if v[j]>v[j+1]:
               temp   = v[j]
               v[j]   = v[j+1]
               v[j+1] = temp

def dietplan(a, b, c):
    j=[]
    m=len(a)
    uni=list(b+c)
    for x in range(len(uni)):
        find=uni[x]
        for k in range(len(a)):
            if find is a[k]:
                del a[k]
                break
        else:
            if find != '':
                j.append(find)

    if j:
        return "CHEATER"
    else:
        bubbleSort(a)
        return "".join(a)

for i in range(input()):
    t=[]
    for j in range(3):
        t.append(list(raw_input()))
    print dietplan(t[0], t[1], t[2])
