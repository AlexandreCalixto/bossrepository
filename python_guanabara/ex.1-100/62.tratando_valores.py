num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero ou 999 para parar: '))
    cont +=1
    soma += num
print(f'Você digitou {cont-1} números e a soma entre eles foi {soma-999}')