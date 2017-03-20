codes = raw_input().split(" ")
a, b = codes
a, b = (int(a), int(b))

if a == 1:
   r=b*4.00
if a == 2:
   r=b*4.50
if a == 3:
   r=b*5.00
if a == 4:
   r=b*2.00
if a == 5:
   r=b*1.50

print("Total: R$ %0.2f" %r)
