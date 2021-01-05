Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp = 102
>>> if temp > 100:
	aguaFerve = True

	
>>> aguaFerve
True
>>> if temp > 100:
	aguaFerve = True
	evaporacao = "muito rapido"

	
>>> aguaFerve
True
>>> evaporacao
'muito rapido'
>>> temp = 90
>>> if temp > 100:
	aguaFerve = True
	evaporacao = "muito rapido"
else:
	aguaFerver = False

	
>>> aguaFerve
True
>>> math.sqrt(8)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    math.sqrt(8)
NameError: name 'math' is not defined
>>> import math
>>> math.sqrt(8)
2.8284271247461903
>>> 1 + 1 + 1 == 3
True
>>> a = True
>>> b = 1
>>> if(a):
	b

	
1
>>> texto = "computação"
if len(texto) > 10:
	print ("texto com mais de 10 caracteres")
else:
	print ("texto com 10 ou menos caracteres")
    
	
>>> x = 1
>>> y = 2
>>> 
x > y or x < y
True
>>> not(x == y)
True

>>> a=0
>>> b = 2
>>> c = 1
>>> if (a > 0):
	if (b > 0):
		print ("Tudo ok para decolagem!")
	else:
		print ("Tanque principal vazio; voando com combustível reserva!")
else:
	if (c > 0):
		print ("Foguete não tem piloto, mas há outros foguetes disponíveis!")

		
Foguete não tem piloto, mas há outros foguetes disponíveis!
>>> 
Digite um número inteiro: 10
>>> numero mod 2
  File "<stdin>", line 1
    numero mod 2
           ^
SyntaxError: invalid syntax
>>> numero %% 2
  File "<stdin>", line 1
    numero %% 2
            ^
SyntaxError: invalid syntax
>>> numero % 2
0
>>> numero % 3
1
>>> numero / 3
3.3333333333333335
>>> numero // 3
3