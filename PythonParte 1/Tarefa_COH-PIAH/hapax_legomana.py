'''EX: hapax_legomana("o, gato, caçava, o, rato")'''
'''Resultado: 0.6'''
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


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas


def hapax_legomana(texto):
    palavras = []

    '''array recebendo lista de sentencas'''
    sentencas = separa_sentencas(texto)
    
    '''laço que lê as sentenças e cria um array de frases pra cada sentença'''
    for sentenca in sentencas:

        #print(sentenca)
        frases = separa_frases(sentenca)

        '''laço que lê as frases'''
        for frase in frases:

            #print(frase)
            '''array recebendo cada palavra do texto com o um elemento'''
            palavras = palavras + separa_palavras(frase)    

    '''var que receberá o numero de palavras que só aparecem uma vez'''
    aparecem_uma_vez = n_palavras_unicas(palavras)
    '''var que receberá a soma das palavras'''
    soma_palavras = len(palavras)

    #print(palavras)
    #print(aparecem_uma_vez)
    #print(soma_palavras)
    
    '''hapax'''
    hapax = aparecem_uma_vez / soma_palavras
    return hapax



