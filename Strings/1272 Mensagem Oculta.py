def msgOculta( str ):
    a = ""
    for i in range(len(str)):
        a += str[i][0]
    return a

for x in range(input()):
    print msgOculta(raw_input().split())