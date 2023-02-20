primeiro = int(input('Digite o 1° valor: '))
segundo = int(input('Digite o 2° valor: '))
print('[ 1 ] Somar')
print('[ 2 ] Multiplicar')
print('[ 3 ] Maior')
print('[ 4 ] Novos numeros')
print('[ 5 ] Sair do programa')
opcao = int(input('>>>> Qual é sua opção? \n'))
while opcao != 5:
    if opcao == 1:
        print(f'A soma entre {primeiro} e {segundo} é igual a {primeiro + segundo}')
        print('=-=-' * 20)
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos numeros')
        print('[ 5 ] Sair do programa')
        opcao = int(input('>>>> Qual é sua opção? \n'))
    elif opcao == 2:
        print(f'A multiplicação entre {primeiro} e {segundo} é igual a {primeiro * segundo}')
        print('=-=-' * 20)
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos numeros')
        print('[ 5 ] Sair do programa')
        opcao = int(input('>>>> Qual é sua opção? \n'))
    elif opcao == 3:
        maior = primeiro
        if maior < segundo:
            maior = segundo
        print(f'O maior numero é : {maior}')
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos numeros')
        print('[ 5 ] Sair do programa')
        opcao = int(input('>>>> Qual é sua opção? \n'))
    else:
        primeiro = int(input('Digite o 1° valor: '))
        segundo = int(input('Digite o 2° valor: '))
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos numeros')
        print('[ 5 ] Sair do programa')
        opcao = int(input('>>>> Qual é sua opção? \n'))  

print('Finalizando o programa!!')            
        
    