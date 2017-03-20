def cripto(word):
        cpy=list(word[:])
        for x in range(len(word)):
            if word[x]>='a' and word[x]<='z' or word[x]>='A' and word[x]<='Z':
               cpy[x]=chr(ord(word[x]) + 3)

        cpy=cpy[::-1];l=len(word)
        for m in range(l/2, l):
            cpy[m]=chr(ord(cpy[m])-1)

        return "".join(cpy)

for i in range(int(raw_input())):
    print cripto(raw_input())