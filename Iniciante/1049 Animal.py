
a=raw_input()
b=raw_input()
c=raw_input()

x = a == "vertebrado"   and b == "ave"      and c == "carnivoro"
y = a == "vertebrado"   and b == "ave"      and c == "onivoro"
z = a == "vertebrado"   and b == "mamifero" and c == "onivoro"
h = a == "vertebrado"   and b == "mamifero" and c == "herbivoro"
f = a == "invertebrado" and b == "inseto"   and c == "hematofago"
j = a == "invertebrado" and b == "inseto"   and c == "herbivoro"
k = a == "invertebrado" and b == "anelideo" and c == "hemetafogo"
l = a == "invertebrado" and b == "anelideo" and c == "onivoro"


if x:
	print "aguia"
elif y:
	print "pomba"
elif z:
	print "homem"
elif h:
	print "vaca"
elif f:
	print "pulga"
elif j:
	print "lagarto"
elif k:
	print "sanguessuga"
elif l:
	print "minhoca"
