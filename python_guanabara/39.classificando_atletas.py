from datetime import date
print('Classificando nossos nadadores!! \n')

atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano

if idade > 25:
    print(f'Você tem {idade} anos e está classificado como MASTER') 
elif idade <= 9:
    print(f'Você tem {idade} anos e é classificado como MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos e é classificado como INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos e é classificado como JUNIOR')
else:
    print(f'Você tem {idade} anos e é classificado como SÊNIOR')