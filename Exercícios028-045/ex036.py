# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('Olá, eu sou a Seve, agente virtual do BancoSv, vou auxiliá-lo no empréstimo para a compra da sua casa dos sonhos.')
casa = float(input('Primeiro digite o valor da casa que você quer comprar: '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos de fincanciamento? '))
pmensal = float(casa / (anos*12))
condemp = 0.3 * salario
print('O valor mensal que será pago, levando em consideração o tempo escolhido, é de R${:.2f}'.format(pmensal))
if pmensal > condemp:
    print('Sinto muito, mas o empréstimo foi negado!')
else:
    print('Parabéns, o empréstimo foi aceito! Você poderá comprar sua casa.')

