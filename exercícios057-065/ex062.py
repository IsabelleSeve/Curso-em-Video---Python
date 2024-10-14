# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos.

print("="*20)
print("10 Termos de uma PA")
print("="*20)
pt = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = pt
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print("{} → ".format(termo), end="")
        termo += razao # ao invés de usar essa expressão, poderia ter usado apenas termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Deseja mostrar mais quantos termos: "))
print("A pregressão foi finalizada com {} termos mostrados".format(total))