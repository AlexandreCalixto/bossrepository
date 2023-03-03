times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitoria', 
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico-GO')
print('-=' *15)
print(f'Lista de Time: {times}')
print('-=' *15)

print(f'Os 5 primeiros colocados do Brasileirão são: {times[0:5]}')
print('-=' *15)
print(f'Os últimos quatro times são: {times[-4:]}')
print('-=' *15)
print(f'Os times em Ordem Alfabética: {sorted(times)}')
print('-=' *15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição')


