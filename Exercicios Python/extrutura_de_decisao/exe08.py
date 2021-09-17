preco1 = float(input("Insira o primero preco\t"))
preco2 = float(input("Insira o segundo preco\t"))
preco3 = float(input("Insira o terceiro preco\t"))

maior = preco1
if preco2 < maior:
    maior = preco2
if preco3 < maior:
    maior = preco3

print(f"compre o produto de R${maior:,.2f}")
