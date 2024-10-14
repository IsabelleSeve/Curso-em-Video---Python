pessoas = []
leves = []
pesadas = []
cont = 0
resp = "S"

while resp == "S":
    cadastro = []
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    cadastro.append(nome)
    cadastro.append(peso)
    pessoas.append(cadastro)

    if peso < 70:
        leves.append(nome)
    else:
        pesadas.append(nome)

    cont += 1
    resp = input('Deseja continuar[S/N]: ').upper()

print("Pessoas cadastradas:")
for pessoa in pessoas:
    print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]}')

print(f'Foram cadastradas: {cont} pessoas')

if leves:
    print('As pessoas mais leves são:')
    for leve in leves:
        print(leve)
else:
    print('Não há pessoas leves cadastradas.')

if pesadas:
    print('As pessoas mais pesadas são:')
    for pesada in pesadas:
        print(pesada)
else:
    print('Não há pessoas pesadas cadastradas.')
