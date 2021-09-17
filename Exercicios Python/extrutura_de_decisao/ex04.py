letra = str(input("Insira uma Letra:\t"))
vogais = ['A', 'E', 'I', 'O', 'U']

if letra[0].upper() in vogais:
    print("VOGAL")
else:
    print("CONSOANTE")
