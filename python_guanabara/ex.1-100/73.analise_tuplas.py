num = (int(input('Digite um numero ')), int(input('Digite outro numero ')), int(input('Digite mais um numero ')), int(input('Digite o ultimo numero ')))
print(f'Voce digite os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es)')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
par = 0
for n in num:
    if n % 2 == 0:
        par +=1
print(f'A quantidade de numeros digitados pares foi de: {par}')
