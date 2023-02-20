print('*' * 100)

nome = str(input('Digite seu nome completo: ')).strip()
print('')
print('Analisando seu nome!! ')
print('')
print(f'Seu nome em maiusculas é: {nome.upper()}')
print(f'Seu nome em minusculas é: {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome)} letras')

separa = nome.split()
print(f'Seu primero nome é {separa[0]} e ele tem {len(separa[0])} letras')