Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10 %3
1
>>> 22%3
1
>>> 2*1**2
2
>>> txt = '2'
>>> print txt
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(txt)?
>>> print (txt)
2
>>> str(TXT)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str(TXT)
NameError: name 'TXT' is not defined
>>> print (str(txt))
2
>>> txt + txt
'22'
>>>  txt = "2"
 
SyntaxError: unexpected indent
>>> txt = "2"
>>> print(txt)
2
>>> teste = input("teste")
teste
>>> print("ola")
ola
>>> 
>>> a = 10
>>> b = 20
>>> c = a
>>> b = c
>>> a = b
>>> print(a, b, c)
10 10 10
>>> a=10
>>> b=5
>>> c=a+b
>>> b=20
>>> print(a,b,c)
10 20 15
>>> a=10
>>> A=10
>>> a=20
>>> a=2*a
>>> A=a+A
>>> print(a)
40
>>> print("olá" 'mundo')
olámundo
>>> x= input("qual sua idade")
qual sua idadea=
>>> a=1
>>> b=2
>>> a=b
>>> b=a
>>> print(a)
2
>>> print(b)
2
>>> a=1
>>> b=2
>>> aux=a
>>> a=b
>>> b=aux
>>> print(a)
2
>>> print(b)
1
>>> 
>>> x= input("qual sua idade")
qual sua idade50
>>> print(x)
50
>>> 1==1
True
>>> 1<>1
SyntaxError: invalid syntax
>>> 1=!1
SyntaxError: invalid syntax
>>> 1!=1
False
>>> 2*2
4
>>> 2**2
4
>>> 2***2
SyntaxError: invalid syntax
>>> 2*3
6
>>> 2**3
8
>>> 2*3
print("olá")
print()
print("bom dia")

