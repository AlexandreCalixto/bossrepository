#interactive help
#help(print)
#print(input.__doc__)


# def contador(i, f, p):
#     """
#     :inicio
#     :fim
#     :passo
#     """
#     c= i
#     while c <= f:
#          print(f'{c}', end='..')
#          c += p
#     print('FIM')

# contador(2, 10, 2)

# help(contador)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
     

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um numero: '))
if par(num):
    print(f'{num} é PAR')
else:
    print(f'{num} é ÍMPAR')