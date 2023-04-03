# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)


# titulo('*** Cadastro de Funcionarios ***')
# titulo('*** Erro do sistema ***')

def terreno(txt):
    print(txt)
    print('-' * 30)
    print()

def area(d, e):
    a = d * e
    print(f'A área do terreno de {d:.2f} de largura x {e:.2f} é igual a {a:.2f}m²')

terreno('Qual o tamanho do terreno em m²? ')
l = float(input('Qual a largura do terreno em m²? '))
c = float(input('Qual o comprimeto do terreno em m²? '))
area(l, c)
