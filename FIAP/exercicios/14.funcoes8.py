def calcularVelocidadeMedia(velocidade, tempo):
    velocidadeMedia = velocidade / tempo
    return velocidadeMedia


velocidade = float(input('Digite a velocidade: '))
tempo = float(input('Digite o tempo da viagem: '))

print(f'A velocidade média da viagem é {(calcularVelocidadeMedia(velocidade, tempo))}')   
