valor = int(1)

while valor:
    if valor == 1:
        print("NÚMERO INVÁLIDO")
        num = float(input("INSIRA UMA NOTA DE 0 A 10:\t"))
    valor = 1 if num <= 0 or num >= 10 else 0
print("CERTO")
