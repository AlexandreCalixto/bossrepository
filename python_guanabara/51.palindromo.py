frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase digitada: {frase} É PALINDROMO')
else:
    print(f'A frase digitada: {frase} NÃO É UM PALINDROMO')