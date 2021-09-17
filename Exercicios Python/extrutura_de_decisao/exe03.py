letra = str(input("Insira uma Letra:\t"))

if letra[0].upper() == str('F'):
    print("FEMININO")
elif letra[0].lower() == str('M'):
    print("MASCULINO")
else:
    print("Sexo inválido")
