def leiaInt(n):
    print('-' * 30)
    while True:
        num = str(input('Digite um numero: '))
        if num.isnumeric():
            return num
        else:
            print('ERRO!! Digite um valor inteiro')


#programa principal
n = int(input('Digite um numero: '))
print(f'Você acabou de digitar o numero {leiaInt(n)}')

