print("*"*50)
print("JOGO DE ADIVINHAÇÃO")
print("*"*50)

numero_secreto = 32
tentativas = 3
rodadas = 1

while (rodadas<=tentativas):

    print(f"Rodada {rodadas} de {tentativas}")
    numero_digitado = int(input("digite um número: "))
    acertou = numero_secreto == numero_digitado
    maior = numero_digitado > numero_secreto
    menor = numero_digitado < numero_secreto

    if (acertou):
        print(f"Parabéns você acertou o número secreto é {numero_secreto}")
        break
    else:
        if(maior):
            print("Você errou ! digitou um número maior")
        elif(menor):
            print("Você errou ! digitou um número menor")

    rodadas+=1

else:
    print("GAME OVER")