'''EX: complexidade_sentenca("o gato, mia. o gato; mia muito.")'''
'''Resultado: 2.0'''
'''versão 01'''

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


def complexidade_sentenca(texto):    
    '''array recebendo lista de sentencas'''
    sentencas = separa_sentencas(texto)

    numero_frases = 0
    
    '''laço que lê as sentenças e cria um array de frases pra cada sentença'''
    for sentenca in sentencas:
        frases = separa_frases(sentenca)

        '''var que vai somando o numero de frases em cada sentença'''
        numero_frases = numero_frases + len(frases)
        
    '''var que receberá a soma das palavras'''
    numero_sentencas = len(sentencas)
    
    '''complexidade'''
    complexidade = numero_frases / numero_sentencas
    return complexidade



