n = int(input("Digite um número inteiro: "))
resultado = "não"
while n > 0:
	ultimo = n % 10
	n = n // 10
	if ultimo == (n % 10):
		resultado = "sim"
		n = 0
print (resultado)
