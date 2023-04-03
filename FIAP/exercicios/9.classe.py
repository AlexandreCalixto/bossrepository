class FichaPessoa():
    #campo - variaveis
    # metodos - funcoes

    def __init__(self, nome, sobrenome, cep, data_nascimento):
        self.nome = nome #campo "nome"
        self.sobrenome = sobrenome
        self.cep = cep
        self.data_nascimento = data_nascimento

    def __str__(self):
        return (f'objeto do tipo fichaPessoa - {self.nome} {self.sobrenome}')

ficha_erick = FichaPessoa(nome='Erick', sobrenome = 'Muller', cep='01010101', data_nascimento = '07/08/1985')
print(ficha_erick)
print(f'Nome: {ficha_erick.nome}')

ficha_samuel = FichaPessoa(nome='Samuel', sobrenome = 'Costa', cep='01010505', data_nascimento = '22/05')
print(ficha_samuel)
print(f'Nome: {ficha_samuel.nome}')

ficha_alexandre = FichaPessoa(nome='Alexandre', sobrenome='Calixto', cep='05545123', data_nascimento='07/06')
print(ficha_alexandre)
print(f'Nome: {ficha_alexandre.nome}')