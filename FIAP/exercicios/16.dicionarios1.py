import sys

nome = "Bruce Wayne"
idade = 30
peso = 92.3

print(f'A variavel nome é do tipo {type(nome)} e tem {sys.getsizeof(nome)} bytes')
print(f'A variavel idade é do tipo {type(idade)} e tem {sys.getsizeof(idade)} bytes')
print(f'A variavel peso é do tipo {type(peso)} e tem {sys.getsizeof(peso)} bytes')