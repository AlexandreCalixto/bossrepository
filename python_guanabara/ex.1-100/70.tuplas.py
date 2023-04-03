cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou o numero {cont[num]}')
resp = ' '
while resp not in 'S':
    resp = str(input('Você quer Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break


