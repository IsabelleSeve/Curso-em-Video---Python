# Crie um programa que tenha um tupla com várias palavras (Não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são suas vogais.

palavras = ("Mano",'Meu','cerebro','nao','funciona',
            'falha','pessoal','caixa','riffle', 'neblina')
print("{:-^60}".format("Palavras"))
print("palavras")
for cont in range(0, len(palavras[::1])):
    a = "a" in palavras[cont]
    e = "e" in palavras[cont]
    i = "i" in palavras[cont]
    o = "o" in palavras[cont]
    u = "u" in palavras[cont]
    print(f'{palavras[cont]} tem as vogais: {a} - {e} - {i} - {o} - {u}')