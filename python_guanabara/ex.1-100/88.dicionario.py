#tuplas ()
#listras []
#Dicionario {}

# dados = {'Nome':'Pedro', 'idade':25}
# print(dados['nome'])
# print(dados[idade])

filme = {'titulo': 'Star Wars', 
         'ano': 1977, 
         'diretor':'George Lucas' 
}
# pega os valores 'Star Wars, 1977, George Lucas
print(filme.values())
# pega as chaves 'titulo', 'ano', 'diretor'
print(filme.keys())
#pega os 2 'titulo', 'star wars', ano, 1977, diretor, George Lucas
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

# dá para colocar um dicionario dentro de uma lista
locadora = []
locadora.append(filme)
print('-----')
print(locadora[0]['ano'])