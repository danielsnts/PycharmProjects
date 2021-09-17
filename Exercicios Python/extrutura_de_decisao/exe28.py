
tipo_carne = str(input("Informe o tipo de carne (F - Filé Duplo A- Alcatra P - Picanha):\t"))
quantidade = float(input("Insira a qunatidade (kg):\t"))
preco = float()
if tipo_carne.upper() == "F":
    preco = quantidade * (4.9 if quantidade <= 5 else 5.8)
elif tipo_carne.upper() == "A":
    preco = quantidade * (5.9 if quantidade <= 5 else 6.8)
elif tipo_carne.upper() == "P":
    preco = quantidade * (6.9 if quantidade <= 5 else 7.8)

pagamento = int(input("Informe o tipo de pagamento(1 - DINHEIRO/ 2 - CRÉDITO:\t"))
if pagamento == 1:
    print(f"PREÇO FINAL R$ {preco*0.95}")
else:

    print(f"PREÇO FINAL R$ {preco:,.2f}")
