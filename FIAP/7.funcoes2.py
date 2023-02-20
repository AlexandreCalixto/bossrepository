def baskhara(a, b, c):
    delta = (b**2) - (4 * a * c)
    if delta > 0:
        raiz_1 = (b * (-1) + delta ** 1/2) / 2 * 1
        raiz_2 = (b * (-1) - delta ** 1/2) / 2 * 1
        return raiz_1, raiz_2
    elif delta == 0:
        raiz_1 = b * (-1) / 2 * a
    else:
        return None


print(baskhara(1, 40, 2))