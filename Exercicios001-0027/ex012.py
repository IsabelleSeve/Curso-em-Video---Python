# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
v = float(input('Qual o valor do produto? '))
vcd = v-v * 0.05
print('O valor do produto com desconto de 5% será de R${:.2f}'.format(vcd))
