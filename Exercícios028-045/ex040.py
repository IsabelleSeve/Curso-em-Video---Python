# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média: 7.0 ou superior: Aprovado

print('Vamos calcular sua nota para saber se você passou de ano, ficou de recuperação'
      'ou foi reprovado.')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print('Sua média é {} e você foi reprovado, sinto muito!'.format(m))
elif 5.0 < m < 6.9:
    print('Sua média foi {}, você pode fazer a recuperação para tentar ser aprovado!'.format(m))
else:
    print('Você foi aprovado! Parabéns!')