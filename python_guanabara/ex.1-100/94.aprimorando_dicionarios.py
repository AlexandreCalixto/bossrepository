jogador = dict()
jogadores = list()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols marcou na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

print('=-'* 30)
#Alinhamento dos parametros abaixo
print(f'{"Cod.":<4}{"Nome":<10}{"Gols":>9}{"Total":>16}')
print('-'*26)
for k, v in enumerate(jogadores):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com esse código {busca}')
    else:
        print()
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}: ')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols')
        print(f'O jogador {jogadores[busca]["nome"]} marcou {jogadores[busca]["total"]} gols')
print('<<<VOLTE SEMPRE>>>')