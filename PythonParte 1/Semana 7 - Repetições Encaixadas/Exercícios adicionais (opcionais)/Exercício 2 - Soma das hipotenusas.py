def é_hipotenusa(n):
    i = 1
    while i < n:
        j = 1
        while j < n:
            if (n**2) == ((i**2)+(j**2)):
                return True
            else:
                j = j + 1
        i = i + 1
    return False
    

def soma_hipotenusas(n):
    soma = 0
    while n >= 1:
        if é_hipotenusa(n) == True:
            soma = soma + n
        n = n - 1
    return soma


#soma_hipotenusas(int(input()))
