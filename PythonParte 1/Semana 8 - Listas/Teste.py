

print("")
lis = [1,2,3,4,5]
lis
#[1, 2, 3, 4, 5]
lis[0]
#1
lis[-2]
4
len(lis)
#5
diferente=["texto", 2, 3.54]
type(diferente[0])
#<class 'str'>
type(diferente[1])
#<class 'int'>
type(diferente[2])
#<class 'float'>
type(diferente)
#<class 'list'>
diferente
#['texto', 2, 3.54]
diferente.append("abc")
diferente
#['texto', 2, 3.54, 'abc']
diferente[3] = 123
diferente
#['texto', 2, 3.54, 123]
diferente[1] = diferente[1] + 1
diferente
#['texto', 3, 3.54, 123]

print("")
flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1

print("")
frutas_exoticas = ["jaboticaba", "cupuacu", "graviola"]
for fruta in frutas_exoticas:
    print ("Eu adoro " + fruta)

print("")
for i in range(5):
    print(i)

print("")
for i in range(3, 5):
    print(i)

print("")#inicio, fim , passo
for i in range(0, 20, 4):
    print(i)

print("")
pares = range (0, 40, 2)
for i in pares: print (i)

print("")
numeros = range (100, 0, -5)
for x in numeros: print (x)

print("")
primos = [2,3,5,7,13]
for i in range(len(primos)):
    primos[i] = primos[i]**3
print(primos)


print("")
animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
print("1")
##for x in animais:
##    print("——> ", x-1)
print("2")
for x in range(len(animais)):
    print("--> ", animais[x])
print("3")
for x in animais:
    print("--> ", x)
print("4")
for x in range(len(animais)):
    print("--> ", x)
print("5")
for x in animais:
    print("--> " + x)


print("O cédigo abaixo imprimiré todos os valores da lista pares.")
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 29, 22, 24, 26, 28, 30]
for x in range(len(pares)):
    print(pares[x])

print("O cédigo abaixo imprimiré todos os valores da lista pares.")
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(len(pares)):
    print(x)
    
print("O cédigo abaixo imprimiré os mL'IItiplos de 5. comegando por 0 e terminando com 45.")
for i in range(0, 50, 5):
    print(i)
    
print("O cédigo abaixo imprimiré os valores da lista pares da posigéo S até a posigéo10. ou seja. 12. 14. 16. 18.20.22.")
##pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 39]
##for x in range(5, 16):
##    print(pares[x])
    
print("Os comandos abaixo imprimiréo os valores: 16. 13, 10.7.")
for i in range(16,4,-3):
    print(i)



print("O cédigo abaixo gera uma lista de nL'Imeros. Analise-o:")
valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)
print(valores)

print("Assinale o cédigo que gera uma lista com os mesmos valores gerados acima:")
print("a")
valores = []
for i in range(1, 16, 2):
    valores.append(i)
print(valores)

print("b")
valores = []
for i in range(1, 10):
    valores.append(i+1)
print(valores)

print("c")
valores = []
for i in range(9, 16, 2):
    valores.append(i)
print(valores)

print("d")
valores = []
for i in range(2, 10, 2):
    valores.append(i)
print(valores)

print("")
animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
print(animais)

#animais[2] = animais.append("piriquito")
animais[1+1] = "piriquito"
print(animais)

print("")
primos = [2,3,5,7,13,17,19]
print (primos)
print (primos[2:4])
print (primos[:4])
print (primos[4:])

print("")
#Clonar Lista
#errado
print("errado")
lista1 = ["vermelho", "verde", "azu1"]
print(lista1)
lista2 = lista1
print(lista2)
lista2[0] = "rosa"
print(lista1)
print(lista2)
##correto
print("")
print("correto")
lista1 = ["vermelho", "verde", "azu1"]
lista2 = lista1[:]
lista2[0] = "rosa"
print(lista1)
print(lista2)

print("")
if "rosa" in lista2:
    print(True)

print("")
print(lista1 + lista2)

print("")
lista3 = lista2 + [1,2]
print(lista1)
print(lista2)
print(lista3)

print("")
lista1_trip = lista1 * 3
print(lista1_trip)

print("")
del lista1[2]
del lista1_trip[2:6]
print(lista1)
print(lista1_trip)

print("")
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(alfabeto[0:13])
print(alfabeto[13:27])
print(alfabeto[1:10])
print(len(alfabeto))
print(alfabeto[:13])
print(alfabeto[:])
print(alfabeto[13:])


print("")
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2)


print("")
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = []
for cns in carnes:
    carnes2.append(cns)
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2)

print("")
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes[:]
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2)


print("")
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
if "ponta de alcatra" in carnes:
    print("XXX")
else:
    if "ponta de alcatra" in carnes2:
        print("YYY")
    else:
        print("ZZZ")


print("")
carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1
print(carnes1)
print(carnes2)
print(carnes3)

print("")
pares = [2, 4, 6, 8, 10]
x = pares * 3
print(x)

print("")
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
x = carnes
del (x[-1])
print(carnes)
print(x)


print("")
























