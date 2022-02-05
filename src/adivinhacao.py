
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = 42

    total_de_tentativas = 3
    rodada = 1

    while(rodada <= total_de_tentativas):

        print("Tentaviva {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu numero: ")
        chute = int(chute_str)

        print("Voce digitou", chute_str)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou !!!")
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o nº secreto")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o nº secreto")

        rodada = rodada + 1

    print("Fim do jogo")
