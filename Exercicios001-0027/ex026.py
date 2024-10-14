# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase pelo teclado: ')).upper().strip() # o upper fopi usado para contabilizar o ¨a¨
# mesmo que ele esteja em maiúcula. O strip foi usado pq pode acontecer da pessoa colocar muitos espaços indesejado e
# isso atrapalhar o código
print(str('Essa frase tem {} ¨a¨'.format(frase.count('a'))))
print('O primeiro ¨a¨ aparece no posição {}'.format(frase.find('a')+1))  # O +1 foi colocado pq o python começa a contar
# a partir do 0, e ai adequa
print('O último ¨a¨ aparece no posição {}'.format(frase.rfind('a')+1))
