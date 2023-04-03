listot = []
pares = []
impares = []
while True:
    listot.append(int(input('Digite um numero: ')))
    resp = str(input('Você quer continuar? [S/N] '))
    if resp in 'nN':
        break
for i, v in enumerate(listot):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-' *30)
print(f'A lista total digitada: {listot}')
print(f'A lista de impares: {impares}')
print(f'A lista de pares: {pares}')