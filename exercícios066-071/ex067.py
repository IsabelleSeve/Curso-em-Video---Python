# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
cont = 0
while True:
    n = int(input("Digite um número inteiro: "))
    print('===Tabuada===')
    if n < 0:
        break
    for c in range(1, 11):
        cont += 1
        print("{} x {:2} = {:3}".format(n, cont, cont * n))
    print("=" * 20)
print("Obrigada!")

