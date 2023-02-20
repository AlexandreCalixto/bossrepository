print('Descubra se você passou de ano')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'Parabéns aluno, tirou notas {n1:.1f} e {n2:.1f}, sua média foi de {media:.1f}')
    print('Você está APROVADO')
elif media <=3:
    print(f'Suas notas {n1:.1f} e {n2:.1f} foram muito baixas, sua média foi de {media:.1f}, você precisa estudar mais para o próximo ano')
    print('Você está REPROVADO e terá que cursar o mesmo ano novamente.')
else:
    print(f'Suas notas {n1:.1f} e {n2:.1f} deram media de {media:.1f}')
    print('Você está de RECUPERAÇÃO')
    print(f'Sua média foi de {media:.1f} e será necessário tirar {10 - media:.1f} na prova de recuperação para passar de ano')
