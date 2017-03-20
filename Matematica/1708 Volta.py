ints=raw_input().split(" ")
ta, tb = int(ints[0]), int(ints[1])
c=0
while (tb-ta)*c < tb:
	c+=1
print "%d" %c
