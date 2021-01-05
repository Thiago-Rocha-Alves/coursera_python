def éPrimo(n):
    proximo = 2
    while proximo <= n:
        if n % proximo == 0:
            if n == proximo:
                return 1
            else:
                proximo = n + 1
        else:
            proximo = proximo + 1
    return 0
            
def maior_primo(n):
    while n < 2:
        m = int(input("Digite um númmero maior ou igual a 2: "))
        n = m
    proximo = 2
    while proximo <= n:
        if éPrimo(proximo) == 1:
            maior = proximo
            proximo = proximo + 1
        else:
            proximo = proximo + 1
    return maior
