largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = largura
y = altura
while altura >= 1:
    while x >= 1:
        if x == largura or x == 1 or y == altura or altura == 1:
            print ("#", end = "")
        else:
            print (" ", end = "")
        x = x - 1
    altura = altura - 1
    print()
    x = largura
