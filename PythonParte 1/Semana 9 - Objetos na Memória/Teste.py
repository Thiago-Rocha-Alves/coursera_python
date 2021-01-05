a = "banana"
b = "banana"
a is b
#True
a = [81, 82, 83]
b = [81, 82, 83]
a is b
#False
a == b
#True

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]

print (lista1 == lista2)
#True

origlist = [52, 76, 34, 55]
origlist*3
#[52, 76, 34, 55, 52, 76, 34, 55, 52, 76, 34, 55]
[origlist] * 3
#[[52, 76, 34, 55], [52, 76, 34, 55], [52, 76, 34, 55]]
newlist = [origlist] * 3
origlist[1] = 99
newlist
#[[52, 99, 34, 55], [52, 99, 34, 55], [52, 99, 34, 55]]
