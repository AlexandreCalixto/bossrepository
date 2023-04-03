#importando tempo e random
from time import sleep
from random import randint

#apenas um charme
print('=-' *30)
print(f"{'Joga na MEGA SENA' :^59}")
print('=-' *30)

#perguntando quantos jogos para sortear
resp = int(input('Quantos Jogos você quer que eu sorteie? '))
#charme
print(f'=-=-=-   SORTEANDO {resp} JOGOS   -=-=-=')
#após responder quantos jogos, o programa dará 0.5 segundos antes de iniciar o for abaixo
sleep(0.5)
#para c até a resposta dada pelo usuario(+1) e 0.5 segundos apos cada random
for c in range(1, resp+1):
    lista = []
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    sleep(0.5)
    lista.sort()
    print(f'{c}° jogo: {lista}')



print('-=-=-=-=  <  BOA SORTE  >  -=-=-=-=')


# from random import randint
# lista = []
# cont = 0
# while True:
#     num = randint(1, 60)
#     if num not in lista:
#         lista.append(num)
#         cont +=1
