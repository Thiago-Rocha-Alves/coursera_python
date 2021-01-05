linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print (linha * coluna, end = "\t")  #end é o parametro para o final, \t é TAB
        coluna = coluna + 1                 #por padrão end = \n, nova linha
    linha = linha + 1
    print()
    coluna = 1
