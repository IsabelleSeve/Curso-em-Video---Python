# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete',
           'dezoito','dezenove','vinte')
resp = 's'
resp = str(input('Deseja começar o programa [s/n]: ')).upper()[0]
while True:
    while  resp == 'S':
        numero = int(input("Digite um número inteiro entre 0 e 20: "))
        if 0 <= numero <=20:
            break
        print('Erro! Tente novamente. ', end='')

    print(f"O número {numero} por extenso é: {extenso[numero]}")
    print('------------------Extenso-------------------------')
    resp = str(input('Deseja acomeçar o programa [s/n]: ')).upper()[0]
    if resp == 'N':
        print('Obrigado!')
        break
