import math

def delta(a, b, c):
    return b**2 - 4*a*c

def main():
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print("Esta equação não possui raízes reais")
    else:
        if d == 0:
            raiz1 = (-b)/(2*a)
            print("A raiz desta equação é", raiz1)
        else:
            raiz1 = ((-b) + math.sqrt(d)) / (2*a)
            raiz2 = ((-b) - math.sqrt(d)) / (2*a)
            print("A primeira raiz é:", raiz1)
            print("A primeira raiz é:", raiz2)
