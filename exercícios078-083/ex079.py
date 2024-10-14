#Crie um programa onde o usuário possa digitar vários valores numéricos e
#cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final serão exibidos todos os valores únicos digitados, em ordem crescentes.
resp = input("Deseja começar o programa [s/n]: ").upper()
valores = list()
while resp == "S":
    valor = int(input("Digite um valor inteiro: "))
    if valor not in valores:
        valores.append(valor)
    else:
        print("Esse valor já foi adicionado!")
    resp = input('Deseja continuar [s/n]? ').upper()

print(f'Os valores digitados foram: {valores}')
valores.sort()
print(f'Em ordem crescente: {valores}')