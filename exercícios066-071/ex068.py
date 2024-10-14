# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
while True:
    computador = randint(1,10)
    numjog = 0
    impar = par = ""
    pi = ""
    venceu = 0
    print("Vamos jogar par ou ímpar? ")
    while pi != "PI":
        numjog = int(input("Escolha um número: "))
        pi = str(input("Você quer par ou ímpar [P/I]: ")).upper().strip()[0]
        if pi == "P":
            if (computador + numjog) % 2 == 0:
                print("Você venceu!!!!!!!")
                venceu += 1
            else:
                print("Você perdeu! :(")
                break
        elif pi == "I":
            if (computador + numjog) % 2 == 1:
                print("Você venceu!!!!!!")
                venceu += 1
            else:
                print("Você perdeu! :(")
                break
        print("Vamos jogar novamente...")
    print(f"Fim de jogo! Você venceu {venceu} vezez.")

