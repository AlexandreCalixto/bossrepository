print('*' * 100)

print('Avaliando seu pedido de empréstimo!!')

emprestimo = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário atual? R$ '))
ano = int(input('Em quantos anos deseja pagar esse empréstimo? '))
prestacao = emprestimo / (ano * 12)

print(f'Para pagar essa uma casa de {emprestimo:.2f} em {ano} anos, a prestação será de R$ {prestacao:.2f}')

if prestacao < salario * 0.33:
    print('Emprestimo aprovado')

print('Emprestimo negado')