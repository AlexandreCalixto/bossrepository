numero = int(input("Digite um Numero: "))
resto = numero % 2

eh_par = (numero % 2 == 0)           # tipo de variavel booleano
eh_positivo = (numero >= 0)     # tipo de variavel booleano
termina_com_zero = (numero % 10 == 0)   # True

eh_par_e_positivo = (eh_par and eh_positivo)
eh_par_ou_positivo = (eh_par or eh_positivo)
inverte_resultado = not(eh_par)

print("E par? " + str(eh_par))
print("E positivo? " + str(eh_positivo))
print("Termina com zero? " + str(termina_com_zero))

print("eh_par e positivo? " + str(eh_par_e_positivo))

