print('*' * 100)
print('Analisando triangulos')

reta1 = float(input('Digite o valor da 1° reta '))
reta2 = float(input('Digite o valor da 2° reta '))
reta3 = float(input('Digite o valor da 3° reta '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Essas retas escolhidas PODEM formar um triangulo')
else:
    print('Essas retas escolhidas NÃO PODEM formar um triangulo')