print('**** Vamos descobrir se o ano escolhido é bissexto ou não ****')

ano = int(input('Qual ano deseja analisar? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano escolhido {ano} é BISSEXTO')
else:
    print(f'O ano escolhido {ano} NÃO É BISSEXTO')    