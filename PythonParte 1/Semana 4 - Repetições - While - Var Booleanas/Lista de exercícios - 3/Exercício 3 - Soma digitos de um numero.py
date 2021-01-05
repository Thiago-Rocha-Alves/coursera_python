n = int(input("Digite um número inteiro: "))
total = 0
while n > 0:
	ultimo = n % 10
	n = n // 10
	total = total + ultimo
print(total)
