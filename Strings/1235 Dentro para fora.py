def df( str ):
    l  = list(str)
    pm = l[0:len(l)/2]
    sm = l[len(l)/2:len(l)]
    return "".join((sm+pm)[::-1])

for x in range(input()):
    print df(raw_input())