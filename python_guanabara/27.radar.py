print('*' * 100)

velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[0;31;41mVocê excedeu o limite de velocidade!!!\033[m')
    print(f'\033[0;33;43mSua multa é de {multa:.2f} R$\033[m')

else:
    print('\033[0;32;42mParabéns, você está dentro da velocidade máxima permitida\033[m')