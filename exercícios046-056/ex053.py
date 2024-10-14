# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsidere espaços
# (uma frase que pode ser lida de trás para frente ou de frente para trás)
# print("Você sabe o que é um palindromo? Um diz-se de ou frase ou palavra que se pode ler, indiferentemente, "
#      "da esquerda para a direita ou vice-versa  ")
#print("Vamos ver se vc consegue pensar em um palindromo?")
#frase = str(input("Digite uma frase: "))
#nespaco = str(len(frase)-frase.count(' '))
#minus = nespaco.lower()
#tamanho = len(frase)
#comeco = 0
#comeco += 1
#for c in range(0,tamanho):
#    minus[0] == minus[:]
#if nespaco[0] == nespaco[0:]:
#   print("É um palíndromo.")
#else:
#    print("Não é um palíndromo.")
#print()

frase = str(input("Digite uma frase: ")).strip().lower()
palavras = frase.split() #você separa a fras eem palavras
junto = "".join(palavras) #junta todas as palavras sem espaços
inverso = ""
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Essa frase é palíndroma.")
else:
    print("Essa frase não é palíndroma.")

#Outra forma
# cria uma var chamada inverso
# inveso = junto[::-1]
# releva o laço for