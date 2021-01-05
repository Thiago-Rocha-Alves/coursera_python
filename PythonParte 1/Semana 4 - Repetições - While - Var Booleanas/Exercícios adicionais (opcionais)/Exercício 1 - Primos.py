n = int(input("Digite um número inteiro: "))
if n < 2:
    print ("não primo")
else:
    proximo = 2
    while proximo <= n:
        if n % proximo == 0:
            if n == proximo:
                print ("primo")
            else:
                print ("não primo")
            proximo = n + 1
        else:
            proximo = proximo + 1
    
        
