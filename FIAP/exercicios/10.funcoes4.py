def calcularVelocidadeMedia():
    distancia = float(input('Digite a distancia percorrida: '))
    tempo = float(input('Digite o tempo da viagem: '))

    velocidadeMedia = distancia/tempo

    print(f'A velocidade media é de: {velocidadeMedia}')

calcularVelocidadeMedia()