import jogoAdivinhacao
import jogoForca

while True:
    escolha = input("Escolha o jogo:\n1-Jogo de Advinhação 2-Jogo da forca ")
    if (escolha == '1'):
        jogoAdivinhacao.jogar()
        break

    elif (escolha == '2'):
        jogoForca.jogar()
        break

    else:
        print("OPÇÃO INVÁLIDA")
        continue