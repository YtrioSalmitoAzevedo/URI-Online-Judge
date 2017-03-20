hrs = raw_input().split()
a,b = hrs
a,b = int(a), int(b)

if b>a:
	if b-a == 0:
		tempo=24
	else:
		tempo=b-a
else:
	tempo=(24-(a-b))

print("O JOGO DUROU %d HORA(S)"%tempo)