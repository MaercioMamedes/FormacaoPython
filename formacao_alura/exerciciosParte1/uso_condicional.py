print("*"*50)
print("JOGO DE ADIVINHAÇÃO")
print("*"*50)

numero_secreto = 32
numero_digitado = int(input("digite um número: "))
acertou = numero_secreto == numero_digitado
maior = numero_digitado > numero_secreto
menor = numero_digitado < numero_secreto

if (acertou):
    print(f"Parabéns você acertou o número secreto é {numero_secreto}")
else:
    if(maior):
        print("Você errou ! digitou um número maior")
    elif(menor):
        print("Você errou ! digitou um número menor")



