def ism(x):
    if x>='a' and x<='z':
        return True
    return False

def isM(x):
    if x>='A' and x<='Z':
        return True
    return False

def rot13( string ):

    for x in range(len(string)):
        if ism(string[x]):
            if chr(ord(string[x])+13) <= 'z':
                string[x]=chr(ord(string[x])+13)
            else:
                pm=(ord(string[x])-ord('a'))-13
                string[x]=chr(ord('a')+pm)

        if isM(string[x]):
            if chr(ord(string[x])+13) <= 'Z':
                string[x]=chr(ord(string[x])+13)
            else:
                pM=(ord(string[x])-ord('A'))-13
                string[x]=chr(ord('A')+pM)

    return "".join(string)

while True:
    try:
        print rot13(list(raw_input()))
    except:
        break