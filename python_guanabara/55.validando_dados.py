sexo = str(input('Informe seu sexo: [M/F]: ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos. Por favo, informe seu sexo: ')).upper()[0].strip()
print(f'Sexo {sexo} registrado com sucesso.')