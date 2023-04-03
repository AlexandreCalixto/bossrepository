aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Qual a média de {aluno["nome"]}? '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

#print(aluno)
#print(f'O aluno {aluno["nome"]} teve média {aluno["media"]} e está {aluno["situação"]}')
print('-' * 20)
for k, v in aluno.items():
    print(f'   - {k} é igual a {v}')