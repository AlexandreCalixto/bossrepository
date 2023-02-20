print('**** PAR OU ÍMPAR ****')

numero = int(input('\033[0;35;45mMe diga um numero qualquer:\033[m '))
resultado = numero % 2
if resultado == 0:
    print(f'O numero {numero}, é par!')
else:
    print(f'O numero \033[0;33;43m{numero}\033[m, é ímpar!')

