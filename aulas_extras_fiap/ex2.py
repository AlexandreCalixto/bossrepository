#um progama que peça 5 numeros e veja qual o maior numero e o menor
cont = 0
menor = 0
maior = 0
for c in range(1, 6):
    numero = int(input(f'Digite o {c}° numero '))
    if c == 1:
        menor = numero
        maior = numero
    else:
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero
print(f'O maior numero é {maior} e o menor é {menor}')


    
    