listaArea=raw_input().split(" ")
a, b, c   = listaArea
(a, b, c) = (float(a), float(b), float(c))
print("TRIANGULO: %0.3f" %( (a*c/2) ) )
print("CIRCULO: %0.3f"   %( 3.14159 * ( pow(c, 2) ) ) )
print("TRAPEZIO: %0.3f"  %( ( (a+b)*c )/2 ) )
print("QUADRADO: %0.3f"  %( b*b ))
print("RETANGULO: %0.3f" %( a*b))
