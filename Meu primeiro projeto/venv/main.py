import dasafio

print("****Escolha o jogo desejado****")
jogo = int(input("(1) - Jogo da advinhacao\n"))

if(jogo == 1):
    dasafio.play()