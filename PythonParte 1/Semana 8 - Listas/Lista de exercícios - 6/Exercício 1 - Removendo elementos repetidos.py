def remove_repetidos (lista):
    lista = sorted(lista)
    nova = []
    for i in lista:
        existe = False
        if len(nova) == 0:
            nova.append(i)
        else:
            for j in nova:
                if i == j:
                    existe = True
            if existe == False:
                nova.append(i)

    return nova


