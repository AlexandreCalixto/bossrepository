print('Convertendo bases de numeros')

numero = int(input('Digite um numero '))
print('Escolhe uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'O numero {numero} convertido para binário é: {bin(numero)}')
elif opcao == 2:
    print(f'O numero {numero} convertido para OCTAL é: {oct(numero)}')
elif opcao == 3:
    print(f'O numero {numero} convertido para HEXADECIMAL é: {hex(numero)}')
else:
    print('Oção invalida, tente novamente')