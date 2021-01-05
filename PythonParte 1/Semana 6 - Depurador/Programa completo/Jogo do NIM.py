def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    while n <= 0 or m <= 0 or m > n:
        print("Oops! Valores inválidos! Tente de novo.")
        print("")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print("")
    if n % (m+1) == 0: #Se n é múltiplo de (m+1)
        print("Você começa")
        vez = "Você"
    else:
        print("Computador começa")
        vez = "O computador"
    while n > 0:
        if vez == "Você":
            numero_escolhido = usuario_escolhe_jogada(n, m)
        else:
            numero_escolhido = computador_escolhe_jogada(n, m)
        print("")
        if numero_escolhido == 1:
            peca = "peça"
        else:
            peca = "peças"
        print(vez, "tirou", numero_escolhido, peca, ".")
        n = n - numero_escolhido
        if n == 1:
            peca = "peça"
            resta = "resta"
        else:
            peca = "peças"
            resta = "restam"
        if n == 0:
            print("Fim do jogo!", vez, "ganhou!")
            return vez
        else:
            print("Agora", resta, "apenas", n, peca, "no tabuleiro.")
            if vez == "Você":
                vez = "O computador"
            else:
                vez = "Você"
        
def computador_escolhe_jogada(n, m):
    numero_maximo = m
    retirar = 0
    restante = 0
    if n <= m:
        retirar = n
    else:
        while numero_maximo > 0 and retirar == 0:
            restante = n - numero_maximo
            if restante % (m+1) == 0:
                retirar = numero_maximo
            else:
                numero_maximo = numero_maximo - 1
    if retirar == 0:
        retirar = m
    return retirar
    
def usuario_escolhe_jogada(n, m):
    print("")
    retirar = int(input("Quantas peças você vai tirar? "))
    while retirar > m or retirar < 1 or retirar > n:
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        retirar = int(input("Quantas peças você vai tirar? "))
    return retirar

def Campeonato():
    rodada = 1
    vitoria_computador = 0
    vitoria_usuario = 0
    while rodada <= 3:
        print("")
        print("**** Rodada", rodada, "****")
        vencedor = partida()
        if vencedor == "O computador":
            vitoria_computador = vitoria_computador + 1
        else:
            vitoria_usuario = vitoria_usuario + 1
        rodada = rodada + 1
    print("")
    print("Placar: Você", vitoria_usuario, "X", vitoria_computador, "Computador")
            
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    c = int(input("2 - para jogar um campeonato "))
    print("")
    if c == 1:
        print("Voce escolheu uma partida isolada!")
        partida()
    else:
        print("Voce escolheu um campeonato!")
        Campeonato()

main()

