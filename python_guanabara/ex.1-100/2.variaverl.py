print('*' *100)

variavel = input('Digite qualquer coisa: ')
print(f'O tipo primitivo desse valor é: {type(variavel)} ')
print(f'Só tem espaços? {variavel.isspace()}')
print(f'É um número? {variavel.isnumeric()}')
print(f'É alfabético? {variavel.isalpha()}')
print(f'É alfanumérico? {variavel.isalnum()}')
print(f'Está em maiusculas? {variavel.isupper()}')
print(f'Está em minusculas? {variavel.islower()}')
print(f'Está capitalizada? {variavel.istitle()}')

print('*' *100)