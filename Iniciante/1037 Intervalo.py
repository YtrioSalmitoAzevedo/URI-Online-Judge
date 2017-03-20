number = float(input())
if number < 0.0000:
       print "Fora de intervalo\n"
elif number >=0.0000 and number <= 25.0000:
       print "Intervalo [0,25]\n"
elif number > 25.0000 and number <= 50.0000:
       print "Intervalo (25,50]\n"
elif number > 50.0000 and number <= 75.0000:
       print "Intervalo (50,75]\n"
elif number > 75.0000 and number <= 100.0000:
       print "Intervalo (75,100]\n"
elif number > 100.0000:
       print "Fora do intervalo\n"
