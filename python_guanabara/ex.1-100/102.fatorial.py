def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um numero num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
     
print('-' *20)
print(fatorial(5))
help(fatorial)