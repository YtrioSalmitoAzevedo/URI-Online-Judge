def balan(s):
	empilhar = []
	for x in s:
			if x == '(':
				empilhar.append(x)
			if x == ')':
				if len(empilhar) > 0:
					empilhar.pop()
				else:
					empilhar.append(x)
	if empilhar == []:
		print "correct"
	else:
		print "incorrect"

while True:
	try:
		str=raw_input()
		balan(str)
	except:
		break