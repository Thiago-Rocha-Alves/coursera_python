n = int(input("Digite o valor de n: "))
if n == 0:
    total = 1
else:
    total = n

while n > 1:
	proximo = n-1
	total = total*proximo
	n = proximo

print(total)
