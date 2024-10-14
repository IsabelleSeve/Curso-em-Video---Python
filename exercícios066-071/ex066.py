# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# (desconsidere a flag)
cont = 0
soma = 0
while True:
    n = int(input("Digite um número inteiro, considere que 999 é a condição de parada: "))
    if n == 999:
        break
    else:
        cont += 1
        soma += n

print("Obrigada pela participação!")
print(f"Dos {cont} números digitados as soma entre eles é de {soma}")