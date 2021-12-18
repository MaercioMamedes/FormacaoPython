from random import randint

def parametrosJogo(x, y, z):
    tentativas = x
    intervalo = y
    numero_secreto = randint(0, intervalo + 1)
    pontuacao = z
    rodada(tentativas, pontuacao, intervalo, numero_secreto)

def escolhaNivel(dificuldade):
    if (dificuldade == 1):
        parametrosJogo(7, 20, 90)

    elif (dificuldade == 2):
        parametrosJogo(5, 75, 95)

    elif (dificuldade == 3):
        parametrosJogo(3, 100, 100)

def rodada(tentativas, pontuacao, intervalo, numero_secreto):
    for rodadas in range(1, tentativas + 1):
        print(f"Rodada {rodadas} de {tentativas}")
        numero_digitado = int(input(f"digite um número de 0 à {intervalo}: "))
        pontos_perdidos = abs(numero_secreto - numero_digitado)
        pontuacao -= pontos_perdidos
        acertou = numero_secreto == numero_digitado
        maior = numero_digitado > numero_secreto
        menor = numero_digitado < numero_secreto
        if (numero_digitado < 0 or numero_digitado > 100):
            print("número inválido")
            continue
        elif (acertou):

            print(f"Parabéns você acertou o número secreto é {numero_secreto}")
            print(f"Você fez {pontuacao} pontos")

            break
        else:
            if (maior):
                print(f"Você errou ! digitou um número maior\n")

            elif (menor):
                print("Você errou ! digitou um número menor\n")

        rodadas += 1
    else:
        if (pontuacao < 0):
            pontuacao = 0
        print(f'O número correto era {numero_secreto}')
        print(f"Você fez {pontuacao} pontos")
        print("GAME OVER")


def jogar():
    print("*" * 50)
    print("JOGO DE ADIVINHAÇÃO")
    print("*" * 50)
    dificuldade = int(input("Escolha o nível de dificuldade: \n 1-Fácil 2-Médio 3-Difícil:  "))
    escolhaNivel(dificuldade)


if (__name__ == "__main__"):
    jogar()