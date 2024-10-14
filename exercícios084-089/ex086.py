# # Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# matriz: coluna x linha
lista1 = []
for c in range(0,3):
    num1 = int(input(f'Digite o número da posição [{c}][0]: '))
    lista1.append(num1)
