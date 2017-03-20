def combinar(a, b):
    rest = []
    j    = []
    menor=min(len(a), len(b))
    if len(b) > len(a):
        rest=b[menor:len(b)]
    if len(a) > len(b):
        rest=a[menor:len(a)]

    for x in range(menor):
        j.append(a[x])
        j.append(b[x])

    if 'rest' in locals():
        for k in range(len(rest)):
            j.append(rest[k])

    return "".join(j)

    for x in range(input()):
        k=map(str, raw_input().split())
        print combinar(k[0].strip(), k[1].strip())