print('**** descobrindo qual o maior e menor numero ****')

num1 = int(input('Digite o 1° numero '))
num2 = int(input('Digite o 2° numero '))
num3 = int(input('Digite o 3° numero '))

#verificando o menor numero
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

#verificando o maior numero
if num1 > num2 and num1 > num3:
    maior  = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O maior numero é {maior} e o menor numero é {menor}')