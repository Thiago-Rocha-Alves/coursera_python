sair = False
lista = []
while sair == False:
    n = int(input("Digite um número: "))
    if n == 0:
        sair = True
    else:
        sair = False
        lista.append(n)
tam = len(lista) - 1
while tam >= 0:
    print(lista[tam])
    tam = tam - 1
