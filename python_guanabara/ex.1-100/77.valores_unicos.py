valor = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print(f'Valor {n} adicionado com sucesso.')
    else:
        print('Valor Duplicado, não vou adicionar.')

    resp = str(input('Você quer Continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('=-' * 30)
valor.sort()
print(f'Você adicionou os numeros {valor}')