# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
print("=== Calculadora de progrssão aritmética ===")
print("="*20)
print("10 Termos de uma PA")
print("="*20)
pt = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
n = 0
decimo = pt + (10 - 1) * razao
# for c in range(0,10,1):   minha forma
for c in range(pt, decimo + razao, razao):
    n += 1
    pa = pt + (n - 1)*razao
    print("{}".format(c), end=" → ")
print("Fim")