# usando python
# from math import factorial

# n = int(input('Digite um numero para calcular seu fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')

#Usando logica matematica
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}',end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -=1
    
print(f'{f}')
