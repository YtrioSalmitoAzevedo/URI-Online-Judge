listNumbers      = raw_input().split(" ")
n1, n2, n3, n4   = listNumbers
(n1, n2, n3, n4) = (float(n1),float(n2),float(n3),float(n4))

media = (n1*2 + n2*3 + n3*4 + n4*1)/10

print("Media: %0.1f" %media)
if media >= 7.0:
	print "Aluno aprovado."
elif media < 5.0:
	print "Aluno reprovado."
elif media >=5.0 and media <= 6.9:
	 print "Aluno em exame."
	 nota = float(input())
	 print("Nota do exame: %0.1f" %nota)
	 rMedia=(media+nota)/2
	 if rMedia >= 5.0:
		print "Aluno aprovado."
	 elif rMedia <= 4.9:
		print "Aluno reprovado."
	 print ("Media final: %0.1f" %rMedia)



