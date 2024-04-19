import random

def gerar_cartas():
    cartas = ["rainha", "rei", "valete", "as", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return random.choice(cartas)

def calcular_valor_carta(carta, pontuacao_jogador):
    if carta in ["rainha", "rei", "valete"]:
        return 10
    elif carta == "as":
        return 1
    else:
        return carta

def jogar_blackjack21():
    pontuacao_jogador1 = 0
    pontuacao_jogador2 = 0

    while pontuacao_jogador1 < 21:
        carta = gerar_cartas()
        pontuacao_jogador1 += calcular_valor_carta(carta, pontuacao_jogador1)
        print("Jogador 1:", carta)
        print("Pontuação:", pontuacao_jogador1 )
        if pontuacao_jogador1 == 21:
            print("Jogador 1 ganhou!\n")
            break
        elif pontuacao_jogador1 > 21:
            print("Jogador 1 estourou!\n")
            break
        else:
            print("Jogador 1 pode pegar outra carta.")

    while pontuacao_jogador2 < 21:
        carta = gerar_cartas()
        pontuacao_jogador2 += calcular_valor_carta(carta, pontuacao_jogador2)
        print("Jogador 2:", carta) 
        print("Pontuação:", "carta", + pontuacao_jogador2)
        if pontuacao_jogador2 == 21:
            print("Jogador 2 ganhou!\n")
            break
        elif pontuacao_jogador2 > 21:
            print("Jogador 2 estourou!\n")
            break
        else:
            print("Jogador 2 pode pegar outra carta.")

jogar_blackjack21()