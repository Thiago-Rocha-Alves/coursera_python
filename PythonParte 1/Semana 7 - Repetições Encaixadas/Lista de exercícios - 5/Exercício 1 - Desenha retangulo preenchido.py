largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = largura
while altura >= 1:
    while x >= 1:
        print ("#", end = "")
        x = x - 1
    altura = altura - 1
    print()
    x = largura
