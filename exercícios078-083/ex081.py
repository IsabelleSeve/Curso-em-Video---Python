# Crie um programa que vai ler vários números e colocar numa lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se valor 5 foi digitado e está ou não na lista.

resp = "s".upper()
lista = []
while resp == "S":
    lista.append(int(input("Digite um número inteiro: ")))
    resp = str(input("Deseja continuar [s/n]? ")).upper()
print(f'Os números registrados foram: {lista}')
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 está presente na lista.')
else:
    print("O número 5 não está presente na lista.")

