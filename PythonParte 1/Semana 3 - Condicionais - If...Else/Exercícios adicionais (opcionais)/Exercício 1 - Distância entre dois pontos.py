import math

xA = int(input("Digite x do primeiro ponto: "))
yA = int(input("Digite y do primeiro ponto: "))
xB = int(input("Digite x do segundo ponto: "))
yB = int(input("Digite y do segundo ponto: "))

dAB = math.sqrt(((xB- xA)**2)+((yB - yA)**2))

if dAB >= 10:
    print("longe")
else:
    print("perto")
