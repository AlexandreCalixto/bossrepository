#importando do modulo calc.py
import calc

#solicitando valores ao usuario
valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

#armazenando a soma
soma = calc.somar(valor1, valor2)

#exibindo a soma
print(f'A soma é {soma}')