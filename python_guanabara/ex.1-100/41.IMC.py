print('*' * 100)
print('Verificando seu peso!! \n')

peso = float(input('Digite qual seu peso: KG '))
altura = float(input('Digite qual sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Você está abaixo do peso, seu IMC é {imc:.2f}')
elif imc > 40:
    print(f'Você está em obesidade mórbida, seu IMC é {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print(f'Parabés, você está no peso ideal, seu IMC é {imc:.2f}')
elif imc >= 25 and imc < 30:
    print(f'Você está com sobrepeso, seu IMC é {imc:.2f}')
else:
    print(f'Você está em obesidade, seu IMC é {imc:.2f}')