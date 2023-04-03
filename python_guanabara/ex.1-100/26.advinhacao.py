from random import randint
print('=-' * 80)
print('Jogo de advinhação')
print('=-' * 80)

numero = int(input('Digite um numero entre 0 e 5: '))
maquina = randint(0,5)
if numero == maquina:
    print('VOCÊ ACERTOU!! PARABÉNS')
else:
    print('Você errou, tente novamente')
print(f'O numero que a maquina escolheu foi {maquina}')
