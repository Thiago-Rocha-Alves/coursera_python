numero = int(input("Digite um número inteiro: "))
unidade = int(numero % 10)
dezena = int(((numero - unidade) / 10) % 10)
print("O dígito das dezenas é", dezena)
