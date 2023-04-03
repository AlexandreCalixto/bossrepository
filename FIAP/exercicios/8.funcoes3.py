def ficha_cadastro(nome, sobrenome, cep, data_nascimento=None):
    #retornar um dicionario
    return {
        'nome': nome,
        'sobrenome': sobrenome,
        'cep': cep,
        'data_nascimento': data_nascimento
    }

nome_pessoa = input('Entre com seu nome: ')
sobrenome_pessoa = input('Entre com seu sobrenome: ')
cep_residencia = input('Entre com seu CEP: ')
data_nascimento = input('Qual sua data de nascimento: ')

ficha_preenchida = ficha_cadastro(
    nome = nome_pessoa,
    cep = cep_residencia,
    sobrenome = sobrenome_pessoa,
    data_nascimento = data_nascimento
)

print(ficha_preenchida)