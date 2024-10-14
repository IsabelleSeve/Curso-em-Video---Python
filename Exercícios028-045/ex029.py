# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.
print('Vamos conferir sua você está seguindos as placas de velocidade? ')
vel = int(input('Digite sua velocidade:'))
multa = int((vel-80)*7)
if vel>80:
    print('Você está correndo demais e por esse motivo terei que te multar em R${},00'.format(multa))
else:
    print('Você está dentro do limite de velocidade, continue assim!')