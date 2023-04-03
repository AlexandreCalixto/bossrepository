print('*' * 80)
diaria  = float(input('Quantos dias de aluguel do carro? '))
km = float(input('Quantos kms foram rodados? '))

print(f'O total a pagar por  é {(diaria * 60) + (km * 0.15):.2f} R$')
