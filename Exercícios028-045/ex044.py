# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição
# de pagamento:
# Á vista dinheiro/pix: 10% de desconto
# Á vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
print('-'*5,'Caixa Eletrônico','-'*5)
v = float(input('Digite o valor do produto: '))
print('[1] À vista dinheiro/pix.')
print('[2] À vista no cartão.')
print('[3] Em até 2x no cartão.')
print('[4] 3x ou mais no cartão')
e = int(input('Escolha a forma de pagamento: '))
dp = v-(v * 0.1)
cd = v-(v*0.05)
cdu = v/2
cdt = (v*0.2)+v
if e == 1:
    print('O valor a ser pago será R${:.2f}'.format(dp))
elif e == 2:
    print('O valor a ser pago será R${:.2f}'.format(cd))
elif e == 3:
    print('O valor a ser pago será R${:.2f}'.format(v))
elif e == 4:
    parcelas = int(input("Em quantas parcelas? "))
    pagamento = cdt / parcelas
    print('O valor a ser pago de {} parcelas será de R${:.2f} por parcela'.format(parcelas,pagamento))
else:
    print('Não temos essa opção!')

