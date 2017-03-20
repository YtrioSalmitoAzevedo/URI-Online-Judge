def led(number):
	qtd=0
	for x in number:
		if x == '1':
			qtd += 2
		elif x == '2':
			qtd += 5
		elif x == '3':
			qtd += 5
		elif x == '4':
			qtd += 4
		elif x == '5':
			qtd += 5
		elif x == '6':
			qtd += 6
		elif x == '7':
			qtd += 3
		elif x == '8':
			qtd += 7
		elif x == '9':
			qtd += 6
		elif x == '0':
			qtd += 6

	print qtd, "leds"

n=int(input())
for x in range(n):
	led(raw_input())
