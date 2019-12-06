import random


def play():
    print("************************")
    print("***Jogo da adivinhação**")
    print("************************")
    print("Você deve adivinhar um numero secreto, para cada tentativa que você errar ira perder",
          "pontos,\nvocê terá um numero de tentativas de acordo com a dificuldade escolhida")

    numero_secreto = random.randrange(1,101)

    print("Escolha a dificuldade:")

    dificuldade = int(input("(1) Dificil - 5 Tentativas\n(2) Médio - 10 Tentativas\n(3) Facil - 20 Tentativas\n"))

    if (dificuldade == 1):
        tentativas = 5
    elif(dificuldade == 2):
        tentativas = 10
    else:
        tentativas = 20

    pontos = 1000

    for rodada in range(1, tentativas + 1):
        print("Rodada {} de {}".format(rodada,tentativas))
        print("Você possui {} pontos".format(pontos))
        chute = int(input("Escolha um numero de 1 a 100\n"))
        print("Você chutou:",chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabens você acertou, o numero secreto é: ",numero_secreto)
            break
        else:
            if(maior):
                print("O numero que você chutou é maior que o numero secreto")
                pontos = pontos - abs(chute - numero_secreto)
            elif(menor):
                print("O numero que você chutou é menor que o numero secreto")
                pontos = pontos - abs(numero_secreto - chute)

    print("Sua pontuação final foi de: ",pontos)
    print("Fim do jogo.")

if(__name__ == "__main__"):
    play()