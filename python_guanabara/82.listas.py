
# pessoas.append(dados[:]) faz uma copia da estrutura de dados
# pessoas = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]
# print(pessoas[2][0]) #Joao

# print(pessoas[1])
temp = []
dados = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    dados.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]' ))
    if resp in 'Nn':
        break
print('=-' * 30)
print(dados)
print(f'Ao todo você cadastrou {len(dados)} pessoas')
print(f'O maior peso foi de {maior} KGs. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'\nO menor peso foi de {menor} KGs', end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()