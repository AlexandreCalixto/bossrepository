from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)


print('JO KEN PO')
print('Sua OPÇÕES: ')

print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogada = int(input('Qual sua jogada? '))
if jogada >= 3:
    print('Jogada Invalida')
else:
    print('=-' *25)
    print(f'O computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogada]}')
    print('=-' *25)

    if computador == 0:
        if jogada == 0:
            print('EMPATE')
        elif jogada == 1:
            print('JOGADOR GANHOU')
        elif jogada == 2:
            print('COMPUTADOR GANHOU')
        else:
            print('Jogada Invalida')

    elif computador == 1:
        if jogada == 0:
            print('COMPUTADOR GANHOU')
        elif jogada == 1:
            print('EMPATE')
        elif jogada == 2:
            print('JOGADOR GANHOU')
        else:
            print('Jogada Invalida')

    else:
        if jogada == 0:
            print('JOGADOR GANHOU')
        elif jogada == 1:
            print('COMPUTADOR GANHOU')
        elif jogada == 2:
            print('EMPATE')
        else:
            print('Jogada Invalida')

#0 PEDRA
#1 PAPEL
#2 TESOURA
     



