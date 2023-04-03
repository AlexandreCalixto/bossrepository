print('***** Calculando seu nome salario!! *****')

salario = float(input('Qual seu salário em R$? '))

if salario > 1250:
    print(f'O seu salario de {salario} R$, com o aumentou passou a {salario * 1.1:.2f} R$')
else:
    print(f'O seu salario de {salario} R$, com o aumento passou a {salario * 1.15:.2f} R$')