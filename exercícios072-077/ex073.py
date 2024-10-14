# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# coloção. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com todos os times em ordem Alfabética.
# D) Em que posição na tabela está o time da Chapecoense.


times = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Bragantino','Fluminense','Atlético-PR','Internacional',
         'Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás','Coritiba')
print('========================================Brasileirão============================================')
print('Os cinco primeiros times da tabela são: ',times[0:5])
print('------------------------------------------------------------------------------------------------')
print('Os últimos quatro colocados da lista são: ', times[:-5:-1]) #ou {times[-4:]}
print('------------------------------------------------------------------------------------------------')
print(f'O time do Corinthians está em {times.index("Corinthians")+1} posição')
print('------------------------------------------------------------------------------------------------')
print('Times em ordem alfabética:', sorted(times))