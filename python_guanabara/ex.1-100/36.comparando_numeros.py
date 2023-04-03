print('Comparando 2 numeros')

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if n1 > n2:
    print(f'O numero {n1} é maior que numero {n2}')
elif n1 < n2:
    print(f'O numero {n2} é maior que numero {n1}')
else:
    print(f'Os valores {n1} e {n2} são iguais.')