numbers = raw_input().split(" ")
a, b, c, d = numbers
a, b, c, d = (int(a), int(b), int(c), int(d))

if b > c and d > a and c+d > a+b:
   if c > 0 and d > 0 and a%2 == 0 :
      print ("Valores aceitos")
else:
      print ("Valores nao aceitos")
