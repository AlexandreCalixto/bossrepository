print('**** A tão sonhada viagem ****')

distancia = float(input('Me diga a distancia da viagem a ser percorrida em kms: '))

if distancia <= 200:
    print(f'Sua jornada de {distancia:.2f} kms, custará {distancia * 0.50:.2f} R$')
else:
    print(f'Sua jornada de {distancia:.2f} kms, custará {distancia * 0.45:.2f} R$')