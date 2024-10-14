# faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis
# sobre ele
a = input('Escreva algo no seu teclado ')
print('O tipo primitivo é:', type(a))
print('O que foi digitado tem letra ou número?', a.isalnum())
print('O que foi digitado é apenas letra?', a.isalpha())
print('O que foi digitado é apenas número?', a.isnumeric())
print('O que foi digitado é apenas espaços? ', a.isspace())
print('O que foi digitado está em maiúsculo?', a.isupper())
print('O que foi digitado está em minúsculo?', a.islower())
