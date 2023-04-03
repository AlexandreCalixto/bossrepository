numero = int(input('Digite um numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[35m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
print(f'\n\033[mO numero {numero} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele É primo')
else:
    print('E por isso ele NÃO É primo')