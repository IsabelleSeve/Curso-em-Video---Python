# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: sobrepeso
# 30 até 40: Obesidade
# acima de 40: Obesidade mórbida

#IMC = Peso ÷ (Altura × Altura)
print('Vamos calcular seu IMC? Vou precisar que você me passe algumas informações.')
peso = float(input('Por me dizer seu peso por favor: '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu IMC deu {:.2f}, e por estar abaixo de 18.5 configura que você está abaixo do peso ideal.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f} e configura que você está no peso ideal!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f} e configura que você está Sobrepeso!'.format(imc))
elif 30 < imc < 40:
    print('Seu IMC é {:.2f} e configura que você está no nível de obesidade!'.format(imc))
else:
    print('Seu IMC é {:.2f} e configura Obesidade mórbida!'.format(imc))