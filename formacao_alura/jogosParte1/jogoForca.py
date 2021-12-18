from random import randint
import desenhos

def lerArquivo():
    lista_palavras = []
    with open("palavras.txt") as arquivo:
        for palavra in arquivo:
            linha = palavra.strip()
            lista_palavras.append(linha)
        indice = randint(0,len(lista_palavras)-1)
    return lista_palavras[indice]

def mostraResultado(palavra_secreta, chute, indice_letra, lista_letras):
    ocorrencia = palavra_secreta.count(chute)
    for x in range(ocorrencia):
        indice = mostraIndices(palavra_secreta, chute, indice_letra)
        lista_letras[indice] = chute
        indice_letra = indice + 1
    if ("_" not in lista_letras):
        return True
    else:
        return False

def recebeLetra(palavra_secreta, lista_letras,erros, acertou):
    print(lista_letras)
    chute = input("Digite uma letra: ")
    chute = chute.lower()
    indice_letra = 0
    if ((chute in palavra_secreta) and (not chute in lista_letras)):
        acertou = mostraResultado(palavra_secreta, chute, indice_letra, lista_letras)
        return erros, acertou

    elif (chute in lista_letras):
        print("Letra já digitada")
        return erros, acertou

    else:
        print("Letra não encontrada")
        erros += 1
        return erros, acertou

def mostraIndices(palavra, letra, indice_letra):
    return palavra.index(letra, indice_letra)

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavra_secreta = lerArquivo()
    enforcou = False
    acertou = False
    lista_letras = ["_" for x in range(len(palavra_secreta))]
    erros = 0
    while(not acertou and not enforcou):
        desenhos.desenha_forca(erros)
        erros, acertou = recebeLetra(palavra_secreta,lista_letras, erros, acertou)
        if( erros == 7):
            enforcou = True
            print("se fudeu")
            desenhos.imprime_mensagem_perdedor(palavra_secreta)
        elif(acertou == True):
            print("Ae ganhou, caralho !!")
            desenhos.imprime_mensagem_vencedor()
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()