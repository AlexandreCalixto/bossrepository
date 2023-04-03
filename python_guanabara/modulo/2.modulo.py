from uteis import numeros

preco = int(input('Digite o preço: R$ '))
print(f'A metade de R${preco:.2f} é R${numeros.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${numeros.dobro(preco):.2f} ')
print(f'Aumentando 10%, temos R${numeros.porcento(preco):.2f}')
