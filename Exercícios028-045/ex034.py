# Faça um programa que leia o salário do funcionário e calcule o vlaor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

print('Estamos fazendo reajustes nos salários dos funcionários da empresa!')
salario = float(input('Digite seu salário por favor: '))
if salario >1250:
    print('Seu novo salário recebeu um aumento de 10%, ficando {}'.format(salario+(salario*0.1)))
else:
    print('Parabéns, você recebeu um aumento de 15%. Com isso seu novo salário vai ser {}'.format(salario+(salario*0.15)))
print('Obrigada pelos seus serviços')