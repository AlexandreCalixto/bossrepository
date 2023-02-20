num_a = float(input('Entre com o valor de A: '))
num_b = float(input('Entre com o valor de B: '))
num_c = float(input('Entre com o valor de C: '))

delta = num_b ** 2 - 4 * num_a * num_c

if delta < 0:
    print('Sem raizes reais')
elif delta == 0:
    x = (num_b * -1) / (2 * num_a)
    print(f'raiz unica: {x}')
else delta > 1:
    x1 = (num_b * -1) + (delta ** (1/2)) / (2 * num_a)
    x2 = ((num_b * -1) - (delta ** (1/2))) / (2 * num_a)
    print(f'Duas raízes: {x1:.4f} e {x2:.4f}')