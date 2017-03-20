
diaX=raw_input().split(" ")
f=int(diaX[1])
lista2=raw_input().split(" : ")
a, b, c=lista2
a, b, c=int(a), int(b), int(c)

diaY=raw_input().split(" ")
k=int(diaY[1])
lista=raw_input().split(" : ")
x, y, z = lista
x, y, z = int(x), int(y), int(z)

segsDiaX = (86400 - (a*3600 + b*60 + c))
segsDiDf = (((k-1) - f) * 86400)
segsDiaY = (x*3600 + y*60 + z)
total    = (segsDiaX + segsDiDf + segsDiaY)

y, t, i, o = total/86400,((total%86400)/3600),(((total%86400)%3600)/60),(((total%86400)%3600)%60)  
print("%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)" %(y, t, i, o))