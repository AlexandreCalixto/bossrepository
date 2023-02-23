resp = 'S'
cont = 0
media = soma = quant = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
media = soma / cont
print(f'Voce digitou {cont} numero(s) e a media {media}')
print(f'O maior numero foi {maior} e o menor {menor}')