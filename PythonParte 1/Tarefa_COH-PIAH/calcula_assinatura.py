'''EX:'''
'''
    texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
'''
'''calcula_assinatura(texto)'''
'''Resultado: [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]'''
'''versão 01'''

import re

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]

    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''

    return re.split(r'[,:;]+', sentenca)


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

############################################################################


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
    
    '''hapax'''
    hapax = aparecem_uma_vez / soma_palavras
    return hapax


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


def tamanho_medio_frase(texto): 
    numero_caracteres_frases = 0
    numero_frases = 0
    
    '''array recebendo lista de sentencas'''
    sentencas = separa_sentencas(texto)
    
    '''laço que lê as sentenças e cria um array de frases pra cada sentença'''
    for sentenca in sentencas:
        
        frases = separa_frases(sentenca)

        '''laço que lê as frases, conta uma frase pra cada loop e soma os caracteres em cada frase'''
        for frase in frases:
            
            '''var que vai somando o numero de caracteres em cada frase'''
            numero_caracteres_frases = numero_caracteres_frases + len(frase)

            '''var que vai somando o numero de frases em cada sentença'''
            numero_frases = numero_frases + 1
    
    '''Tamanho médio de frase'''
    media_frase = numero_caracteres_frases / numero_frases
    
    return media_frase


############################################################################


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    tamanho_medio = tamanho_medio_palavras(texto)

    type_token = relacao_type_token(texto)

    hapax = hapax_legomana(texto)

    media_sentenca = tamanho_medio_sentenca(texto)

    complexidade = complexidade_sentenca(texto)

    media_frase = tamanho_medio_frase(texto)

    calcula_ass = [tamanho_medio, type_token, hapax, media_sentenca, complexidade, media_frase]

    return calcula_ass
