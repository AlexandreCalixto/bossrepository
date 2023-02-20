print('=' * 15)
print('10 TERMOS DE UMA PA')
print('=' * 15)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))

decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    termo += razao
    print(f'{c}', end=' → ' )
print('ACABOU')
