from time import sleep
from random import randint
jogo = list()
quant = int(input('Quer gerar quantos jogos? '))
for j in range(1, quant+1):
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    print(f'Jogo {j}: {sorted(jogo)}')
    sleep(.5)
    jogo.clear()