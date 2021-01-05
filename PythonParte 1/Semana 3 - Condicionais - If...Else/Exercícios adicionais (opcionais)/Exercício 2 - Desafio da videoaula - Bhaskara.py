import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = b**2 - 4*a*c

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        x = (-b)/(2*a)
        print("a raiz desta equação é", x)
    else:
        x1 = ((-b) + math.sqrt(delta)) / (2*a)
        x2 = ((-b) - math.sqrt(delta)) / (2*a)
        if x1 <= x2:
            ordem = str(x1) + " e " + str(x2)
        else:
            ordem = str(x2) + " e " + str(x1)
        print("as raízes da equação são", ordem)
