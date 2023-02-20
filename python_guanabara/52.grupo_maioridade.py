from datetime import date

atual = date.today().year

c = 0
maior = 0
menor = 0
for c in range(0,7):
    c +=1
    ano = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    idade = atual - ano
    if idade >= 18:
        maior +=1
    else:
        menor +=1
print(f'Ao todos tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
