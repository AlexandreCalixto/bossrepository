palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
print(f'{palavra}', end='')
for p in palavra:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end= ' ')