# desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens até 200km e R$0,45 para viagens mais longas

print('-'*7+'Site de Passagens'+'-'*7)
km = int(input('Primeiro diga quantos Kms terá a viagem: '))
if km<=200:
    print('As passagens para essa viasgem estão saindo por R${},00'.format(int((km*0.5)+km)))
else:
    print('Será uma viagem longuinha, as passagens estão saindo por R${},00'.format(int((km*0.45)+km)))
print('Boa Viagem!')