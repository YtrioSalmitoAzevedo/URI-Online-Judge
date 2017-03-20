import math

l1xy=raw_input().split(" ")
l2xy=raw_input().split(" ")

x1, y1 = l1xy
x2, y2 = l2xy

x1, y1 = (float(x1), float(y1))
x2, y2 = (float(x2), float(y2))

distancia = math.sqrt( (pow(( x2 - x1 ),2) + pow(( y2 - y1 ),2)) )

print("%0.4f" %distancia)
