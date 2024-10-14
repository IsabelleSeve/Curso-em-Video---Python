#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora usando o laco for.
w = 0
n = int(input("Digite um número inteiro e te retornaremos a tabuada dele: "))
print('===Tabuada===')
for c in range(0, 10, 1):
    w += 1
    print("{} x {:2} = {:2}".format(n, w, w*n))
