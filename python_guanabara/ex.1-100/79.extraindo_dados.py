valores = []
while True:
    valores.append(int(input('Digite um numero: ')))
    resp = str(input('Você quer Continuar? S/N '))
    if resp in 'Nn':
        break
    
print('-=' *30)
print(f'Você digitou {len(valores)} elemento(s)')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista.')