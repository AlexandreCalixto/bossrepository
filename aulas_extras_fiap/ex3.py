#pegar os numeros pares de 0 a n, sendo que n é digitado pela pessoa
#retornar como lista

n = int(input('Digita um numero: '))
lista_pares = []
cont = 0

while cont <= n:
    if cont % 2 == 0:
        lista_pares.append(cont)
    cont += 1
print(lista_pares)