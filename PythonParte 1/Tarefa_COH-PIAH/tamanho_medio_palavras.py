'''EX: tamanho_medio_palavras("o gato, mia. o gato; mia muito.")'''
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


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def tamanho_medio_palavras(texto):
    '''var que receberá a soma dos tamanhos das palavras'''
    tamanho_palavras = 0
    soma_palavras = 0

    '''array recebendo lista de sentencas'''
    sentencas = separa_sentencas(texto)
    
    '''laço que lê as sentenças'''
    for sentenca in sentencas:
        
        frases = separa_frases(sentenca)

        '''laço que lê as frases'''
        for frase in frases:

            palavras = separa_palavras(frase)
            
            '''var que vai somando o numero de palavras'''
            soma_palavras = soma_palavras + len(palavras)

            '''laço que lê as palavras e somará os tamanhos de todas as palavras do array'''
            for palavra in palavras:

                tamanho_palavras = tamanho_palavras + len(palavra)
                
    '''média'''
    tamanho_medio = tamanho_palavras / soma_palavras
    return tamanho_medio



