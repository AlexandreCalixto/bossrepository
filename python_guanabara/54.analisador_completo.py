somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        totmulher20 += 1
media = somaidade / 4

print(f'A media de idade é {media:.0f} anos')
print(f'O nome do HOMEM mais velho é {nomevelho} e a idade dele é {maioridadehomem} anos')
print(f'Há {totmulher20} mulheres com menos de 20 anos')