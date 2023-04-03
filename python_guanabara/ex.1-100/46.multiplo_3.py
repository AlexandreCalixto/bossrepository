soma = 0
cont = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        cont = cont +1
        soma = soma + cont
        
print(f'A soma de todos os valores é: {soma}')
