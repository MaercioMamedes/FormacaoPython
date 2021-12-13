print("*"*50)
print("JOGO DE ADIVINHAÇÃO")
print("*"*50)

numero_secreto = 32
tentativas = 3

for rodadas in range(1,tentativas+1):

    print(f"Rodada {rodadas} de {tentativas}")
    numero_digitado = int(input("digite um número de 0 à 100: "))


    acertou = numero_secreto == numero_digitado
    maior = numero_digitado > numero_secreto
    menor = numero_digitado < numero_secreto

    if (numero_digitado<0 or numero_digitado>100):
        print("número inválido")
        continue
    elif (acertou):
        print(f"Parabéns você acertou o número secreto é {numero_secreto}")
        break
    else:
        if(maior):
            print(f"Você errou ! digitou um número maior")

        elif(menor):
            print("Você errou ! digitou um número menor")

    rodadas+=1

else:
    print("GAME OVER")


