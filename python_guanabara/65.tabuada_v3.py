
while True:
    numero = int(input('Digite um numero para saber sua tabuada: '))
    if numero < 0:
        break
    for c in range(0, 11):
        print(f'{numero} x {c} = {numero * c}')
print('Encerrando a Tabuada...')