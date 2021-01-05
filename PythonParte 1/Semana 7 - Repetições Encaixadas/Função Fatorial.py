
def Fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)

def main():
    n = int(input("Digite um número inteiro positivo: "))
    while n >= 0:
        Fatorial(n)
        n = int(input("Digite um número inteiro positivo: "))

main()
        
