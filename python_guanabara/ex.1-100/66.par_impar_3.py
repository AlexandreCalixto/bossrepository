from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('[P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            v +=1
        else:
            print('Você PERDEU')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            v +=1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente. . . ')
print(f'GAME OVER! Você venceu {v} vezes.')