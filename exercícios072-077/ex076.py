# Crie um programa que tem uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular
# Fazer algo bonito e apresentável.

mercadorias = ('Caneta',4,'Lápis',3,'Tesoura',5,'Fichário',30,'Caderno',25)
nvprodutos = mercadorias[::2]
pcprodutos = mercadorias[1::2]
print("|","=" * 36,"|")
print(f'|{"Lista de produtos":^38}|')
print("|","=" * 36,"|")
for loja in range(0,len(nvprodutos[::])):
    #print(f'{(nvprodutos[loja]), (pcprodutos[loja])}')
    print("|{:-<31}R${:2},00|".format(nvprodutos[loja],pcprodutos[loja]))
print("|","=" * 36,"|")
