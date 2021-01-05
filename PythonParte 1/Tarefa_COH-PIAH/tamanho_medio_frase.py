'''EX: tamanho_medio_frase("o gato, mia. o gato; mia muito.")'''
'''Resultado: 6.75'''
'''versão 02'''

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


def tamanho_medio_frase(texto): 
    numero_caracteres_frases = 0
    numero_frases = 0
    
    '''array recebendo lista de sentencas'''
    sentencas = separa_sentencas(texto)
    #sentencas = ([o gato, mia], [o gato; mia muito.])
    
    '''laço que lê as sentenças e cria um array de frases pra cada sentença'''
    for sentenca in sentencas:
    #[o gato, mia],
    #[o gato; mia muito.]
        
        frases = separa_frases(sentenca)
        #frases = ([o gato], [mia])
        #frases = ([o gato], [mia muito])

        '''laço que lê as frases, conta uma frase pra cada loop'''
        for frase in frases:
        #[o gato]
        #[mia]
        #[o gato]
        #[mia muito]

            '''var que vai somando o numero de frases em cada sentença'''
            numero_frases = numero_frases + 1

            palavras = separa_palavras(frase)

            '''laço que lê as palavras, soma os caracteres em cada palavra'''
            for palavra in palavras:

                '''var que vai somando o numero de caracteres em cada palavra'''
                numero_caracteres_frases = numero_caracteres_frases + len(palavra)

    '''Tamanho médio de frase'''
    media_frase = numero_caracteres_frases / numero_frases
    
    return media_frase



