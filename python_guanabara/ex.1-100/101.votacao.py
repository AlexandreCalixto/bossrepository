print('*' *100)
def voto(idade):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos. NÃO VOTA'
    elif idade >= 18 and idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'

nasc = int(input('Ano de nascimento: '))
print(voto(nasc))