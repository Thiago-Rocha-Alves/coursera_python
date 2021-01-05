


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve
    devolver o grau de similaridade nas assinaturas.'''

    diferencas = []
    i = 0
    soma = 0
    qtd_tracos = len(as_b)

    while i < qtd_tracos:
        
        diferencas.append(abs(as_a[i] - as_b[i]))
        
        soma = soma + diferencas[i]
        
        i = i + 1

    Sab = soma / 6

    return Sab

'''aluno infectado:'''
#as_b = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]

#as_a = [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]


#compara_assinatura(as_a, as_b)
