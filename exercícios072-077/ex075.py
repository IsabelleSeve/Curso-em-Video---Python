# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9     ok
# B) Em que posição foi digitado o primeiro valor 3.        ok
# C) Quais foram os números pares.            ok

a = int(input("Digite um valor inteiro: "))
b = int(input("Digite um valor inteiro: "))
c = int(input("Digite um valor inteiro: "))
d = int(input("Digite um valor inteiro: "))
tupla = a,b,c,d
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if tupla == 3:
    print(f'O primeiro número 3 apareceu na posição: {tupla.index(3) + 1}')
else:
    print('Não foi digitado nenhum número 3.')
print(f'Os números pares são: ')
for tupla in range (a,d+1):
    if tupla % 2 == 0:
        print(tupla)