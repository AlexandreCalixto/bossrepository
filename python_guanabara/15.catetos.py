from math import hypot
oposto = float(input('Qual o valor do cateto oposto? '))
adjacente = float(input('Qual o valor do cateto adjacente? '))
hipotenusa = hypot(oposto , adjacente)
print(f'A hipotenusa vale: {hipotenusa:.2f}')