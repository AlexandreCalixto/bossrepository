from random import randint
print('=-' * 80)
print('Jogo de advinhação')
print('=-' * 80)
print('Sou seu computador')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
numero = int(input('Qual é o seu palpite? '))
maquina = randint(0,10)
c = 1
while numero != maquina:
    if numero < maquina:
        print('Mais... Tente outra vez.')
        numero = int(input('Qual é o seu palpite? '))
    elif numero > maquina:
        print('Menos... Tente mais um vez.')
        numero = int(input('Qual é o seu palpite? '))
    c += 1
print('Acertou!!!')
print(f'Você precisou de {c} tentativas!!')