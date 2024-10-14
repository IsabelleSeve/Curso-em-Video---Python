# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar.
# Considere: US$1.00=RS$3,27
print('Vamos calcular quantos dólates você tem com o dunheiro em reais que está na sua carteira?')
v = float(input('Quanto de dinheiro você tem na carteira? '))
c = v//3.27
print('Com R${:.2f} você consegue comprar US${:.2f} '.format(v,c))