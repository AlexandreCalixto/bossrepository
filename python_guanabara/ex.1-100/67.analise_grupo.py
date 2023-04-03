tot18 = 0
toth = 0
totmul = 0
while True:
    print('-' *25)
    print('CADASTRE UMA PESSOA')
    print('-' *25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totmul += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {tot18}')
print(f'O total de homens cadastrados: {toth}')
print(f'O total de mulheres com menos de 20 anos: {totmul}')




    # 
    # 
    
    # while continuar == 'S':
    #     idade = int(input('Idade: '))
    #     sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    #     continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    #     totpes += 1
    # print(f'O total de pessoas cadastradas foi {totpes}')