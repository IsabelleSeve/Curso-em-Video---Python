# Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário com 15% de aumento
s = float(input('Qual o seu salário? '))
sca = s+(s*0.15)
a = s*0.15
print('Seu sálario teve o aumento de R${:.2f}, resultando em R${:.2f}'.format(a,sca))