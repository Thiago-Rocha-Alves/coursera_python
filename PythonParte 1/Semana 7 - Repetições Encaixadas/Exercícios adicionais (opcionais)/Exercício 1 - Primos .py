def éPrimo(n):
    proximo = 2
    while proximo <= n:
        if n % proximo == 0:
            if n == proximo:
                return True
            else:
                proximo = n + 1
        else:
            proximo = proximo + 1
    return False

def n_primos(n):
    contador = 0
    while n >= 2:
        if éPrimo(n) == True:
            contador = contador + 1
        n = n - 1
    return contador


#n_primos(int(input()))
