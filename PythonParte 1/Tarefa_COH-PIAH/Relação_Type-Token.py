'''Ex: relação_type_token("o, gato, caçava, o, rato")'''
'''Resultado: 0.8'''
'''versão 01'''
'''thiago alterou'''
#comentario

import re

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def relacao_type_token(texto):
    palavras = []
    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        
        frases = separa_frases(sentenca)

        for frase in frases:
            palavras = palavras + separa_palavras(frase)
    
    '''Recebe o número de palavras diferentes'''
    palavras_diferentes = n_palavras_diferentes(palavras)

    '''Recebe o número total de palavras'''
    soma_palavras = len(palavras)

    '''Relação Type Token'''
    type_token = palavras_diferentes / soma_palavras
    return type_token
    

        
