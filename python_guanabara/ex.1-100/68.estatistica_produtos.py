totcompra = prodmil = menor = cont = 0
barato = ''
print('-' *25)
print('LOJA SUPER BARATÃO')
print('-' *25)
while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$ '))
    cont += 1
    totcompra += preco
    if preco > 1000:
        prodmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '  
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de: {totcompra}')
print(f'Temos {prodmil} custando mais de R$ 1000.00')
print(f'O produto mais barato foi: {barato} custou R$: {menor}')
    
