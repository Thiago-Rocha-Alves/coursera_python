def soma(x, y):
	return x + y

#print(soma(10,20))
#30

def texto():
	return "Texto"

#texto

def Nome_Time ():
	return "Flamengo"

#Nome_Time()
#'Flamengo'

print("02")

def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)


print("03")

def total_Caracteres1 (x, y, z):
    return len(x)+len(y)+len(z)

#def total_Caracteres2 (x, y, z):
    #return len(x,y,z)

#def total_Caracteres3 (x, y, z):
    #return sum(len(x)+len(y)+len(z))

##def total_Caracteres4 (x, y, z):
##    return sum(len(x,y,z))

print(total_Caracteres1("ABC", "AB", "A"))
#total_Caracteres2("ABC", "AB", "A")
#total_Caracteres3("ABC", "AB", "A")
##total_Caracteres4("ABC", "AB", "A")


print("04")

import math

def suspense(x):
    return math.sqrt(x)


print("05")

##leitura():
##    x = -1
##    while x > 0:
##        x = int(input("Digite um valor: "))
##    return x

def leitura1():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x

##leitura():
##    x = -1
##    while x <= 0:
##        x = int(input("Digite um valor: "))
##    return x

def leitura2():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x

def leitura3():
    x = -1
    while x > 0:
        x = int(input("Digite um valor: "))
    return x


print("1")
leitura1()
print("2")
leitura2()
print("3")
leitura3()
