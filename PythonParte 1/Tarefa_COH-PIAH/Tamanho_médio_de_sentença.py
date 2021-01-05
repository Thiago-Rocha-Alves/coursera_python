'''EX: tamanho_medio_sentenca("o gato, mia. o gato; mia muito.")'''
'''Resultado: 14.5'''
'''versão 01'''


import re


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def tamanho_medio_sentenca(texto):
    '''Recebe a lista de sentenças'''
    sentencas = separa_sentencas(texto)
    
    '''Guarda o número de caracteres na sentença'''
    numero_caracteres = 0

    '''Laço que percorre a lista de sentenças e guarda o número de caracteres'''
    for sentenca in sentencas:
        numero_caracteres = numero_caracteres + len(sentenca)
        
    '''Tamanho médio da sentença'''
    media = numero_caracteres / len(sentencas)
    return media
