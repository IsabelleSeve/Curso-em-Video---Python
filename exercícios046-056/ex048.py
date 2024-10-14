#Faça um programa que calcule a soma entre todos os números ímpares entre são múltiplos
# de três e que se encontram no intervalo de 1 até 500.
s = 0
for c in range(0,500):
    if c%2!=0 and c%3==0:
        s += c
print('A soma dos números impares de 1 até 500 é {}'.format(s))
# Outras formas de fazer
# for cont in range(1, 501, 2)
#   if cont % 3 == 0:
#   print(cont) # ia mostrar todos os valores ímpares de 1 até 500