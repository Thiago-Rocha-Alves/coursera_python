Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5 > 3
True
>>> 18 == 9*2
True
>>> x = 15562
>>> x < 0
False

>>> type(False)
<class 'bool'>
>>> x < 0 and x**2 > 100
False
>>> x < 0 or x**2 > 100
True
>>> x > 0
True
>>> not x > 0
False
>>> fizerSol = True
>>> forFeriado = False
>>> vouParaPraia = fizerSol and forFeriado
>>> vouParaPraia
False
>>> y = 50

>>> y = 50
>>> y
50
>>> x > 0 and not y == 50 or x + y == 150
False
>>> ((x > 0) and (not y == 50)) or (x + y == 150)
False

>>> x = 5
>>> y = 3
>>> x > y
True
>>> x = 5
>>> y = 3
>>> z = 7
>>> x > y and x < z
True
>>> idade=15
>>> maioridade=18
>>> pode_dirigir = idade >= maioridade
>>> print (pode_dirigir)
False

>>> x = 10
>>> y = 15
>>> z = 25
>>> print(x == z - y and z != y - x or not y != z - x)
True
>>> x = 10
>>> y = 20
>>> z = 30
>>> 
