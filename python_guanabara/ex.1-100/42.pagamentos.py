print('Você quer pagar quanto?!?!?!')

preco = float(input('Qual o preço das compras? R$ '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista, no dinheiro ou cheque \n[ 2 ] à vista no cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão?')

opcao = int(input('Qual a opção de pagamento escolhida? '))

if opcao == 4:
    parcelas = int(input('Em quantas parcelas você quer dividir? '))
    print(f' Sua compra será parcelada em {parcelas}x de {(preco * 1.2) / parcelas:.2f} com juros ')
elif opcao == 1:
    print(f'Você escolheu a vista em dinheiro ou cheque e terá um desconto de 10%, o valor a ser pago é: {preco * 0.9:.2f} R$')
elif opcao == 2:
    print(f'Você escolheu a vista no cartão e terá um desconto de 5%, o valor a ser pago é: {preco * 0.95:.2f} R$')
elif opcao == 3:
    print(f'Você escolheu a parcelar em 2x, o valor a ser pago é: {preco:.2f} R$ em 2x de {preco / 2:.2f} R$')
else:
    print('Opção invalida, tente novamente.')