# Crie um programa que leia dois valores e mostre o menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

menu = 4
resp = "S"
resp = str(input("Deseja começar o programa? ")).strip().upper()[0]
while menu == 4 and resp == "S":
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: "))
    menu = int(input("""--------- Menu ---------
| [1] Soma             |
| [2] Multiplicar      | 
| [3] Maior            |
| [4] Novos números    |
| [5] Sair do programa |
--------- Menu ---------
Escolha uma das opções: """))
    if menu == 1:
        print("Resposta: ",n1 + n2)
    elif menu == 2:
        print("Resposta: ",n1 * n2)
    elif menu == 3:
        if n1 > n2:
            print("{} é maior".format(n1))
        else:
            print("{} é maior".format(n2))

print("Obrigada!")

