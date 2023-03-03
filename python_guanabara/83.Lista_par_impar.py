# lista= []
# par = []
# impar = []
# for c in range(1,8):
#     num = int(input(f'Digite o {c}° valor: '))
#     lista.append(num)
#     for i, v in enumerate(lista):
#         if v % 2 == 0:
#             par.append(v)
#         if v % 2 == 1:
#             impar.append(v)
# print(lista)
# print(sorted(par))
# print(sorted(impar))

numero = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    if valor % 2 == 1:
        numero[1].append(valor)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores ímpares digitados forasm: {numero[1]}')
