n = int(input("Digite o valor de n: "))
i = 1
proximo = 1
while proximo <= n:
    if i % 2 != 0:
        print(i)
        proximo = proximo + 1
        i = i + 1
    else:
        i = i + 1
        
