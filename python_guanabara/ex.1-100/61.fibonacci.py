termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 0
print('~'* 50)
while c <= termos:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1
print(' → FIM')