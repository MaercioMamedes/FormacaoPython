from random import randint

print("*"*50)
print("JOGO DE ADIVINHAÇÃO")
print("*"*50)

tentativas = 5
pontuacao = 75
intervalo = 50
numero_secreto = randint(0,intervalo + 1)

dificuldade = int(input("Escolha o nível de dificuldade: \n 1-Fácil 2-Médio 3-Difícil"))

if (dificuldade == 1):
    tentativas = 7
    intervalo = 20
    numero_secreto = randint(0,intervalo + 1)
    pontuacao = 50

elif(dificuldade == 3):
    tentativas = 3
    intervalo = 100
    numero_secreto = randint(0,intervalo + 1)
    pontuacao = 100



for rodadas in range(1,tentativas+1):

    print(f"Rodada {rodadas} de {tentativas}")
    numero_digitado = int(input(f"digite um número de 0 à {intervalo}: "))

    pontuacao = pontuacao - abs(numero_secreto - numero_digitado)
    acertou = numero_secreto == numero_digitado
    maior = numero_digitado > numero_secreto
    menor = numero_digitado < numero_secreto

    if (numero_digitado<0 or numero_digitado>100):
        print("número inválido")
        continue
    elif (acertou):
        
        print(f"Parabéns você acertou o número secreto é {numero_secreto}")
        print(f"Você fez {pontuacao} pontos")
        

        break
    else:
        if(maior):
            print(f"Você errou ! digitou um número maior\n")

        elif(menor):
            print("Você errou ! digitou um número menor\n")

    rodadas+=1

else:
    print(f'O número correto era {numero_secreto}')
    print(f"Você fez {pontuacao} pontos")
    print("GAME OVER")
