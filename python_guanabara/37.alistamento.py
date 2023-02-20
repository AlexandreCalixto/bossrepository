from datetime import date

atual = date.today().year
print('*' *100)
print('Você deve ser alistar no serviço militar obrigatório? \n')

print('Digite m para masculino ou f para feminino \n')
sexo = str(input('Qual seu sexo? ')).upper().strip()

if sexo == 'M':
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc

    if idade > 18:
        print(f'Você tem {idade} anos e passou da hora de alistamento, você deveria ter se alistado há {idade - 18} anos.')
    elif idade == 18:
        print(f'Você tem {idade} anos e está na hora de se alistar.')
    else:
        print(f'Você tem {idade} ano e ainda faltam {18 - idade } anos para se alistar.')
else:
    print('Você não precisa se alistar no serviço militar obrigatório.')
