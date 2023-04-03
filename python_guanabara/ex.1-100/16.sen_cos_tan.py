from math import radians, sin, cos, tan
print('*' * 100)
angulo = float(input('Digite um angulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O angulo de {angulo}, tem o seno {seno:.2f}, cosseno de {cosseno:.2f} e a tangente {tangente:.2f}')