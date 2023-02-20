print('=' * 15)
print('10 TERMOS DE UMA PA')
print('=' * 15)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))

c = 1
resultado = 0
while c < 10:
    print(f'{termo}', end=' → ')
    termo += razao
    c +=1
print('ACABOU')