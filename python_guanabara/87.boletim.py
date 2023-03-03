from time import sleep
infos = list()
temp = list()
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    temp.append((temp[1] + temp[2]) / 2)
    infos.append(temp[:])
    temp.clear()
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Opção inválida. Por favor, coloque S ou N: ')).strip().upper()[0]
    if 'N' in escolha:
        break
sleep(0.5)
print('-=' * 10)
print('Calculando média...')
print('-=' * 10)
sleep(0.5)
print('No. NOME       MÉDIA')
print('-' * 22)
for c in range(len(infos)):
    sleep(0.5)
    print(f'{c:<3} {infos[c][0]:<10} {infos[c][3]:4}')
print('-' * 22)
while True:
    numero_do_aluno = int(input('Deseja ver as notas de qual aluno? [999 para finalizar]: '))
    if numero_do_aluno == 999:
        break
    while numero_do_aluno != 999 and numero_do_aluno > len(infos) - 1:
        numero_do_aluno = int(input('Número de aluno inválido. Por favor, acesse uma posição válida: '))
    print(f'Notas de {infos[numero_do_aluno][0]}: {infos[numero_do_aluno][1]} e {infos[numero_do_aluno][2]}')
print('-=' * 21)
print('Finalizando...')
sleep(1)
print('Obrigado pela preferência! Volte Sempre :)')
print('-=' * 21)