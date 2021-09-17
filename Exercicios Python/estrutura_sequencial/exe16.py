cobertura = float(input("Insira a medida a ser pintada em m^2\:\t" ))
litros_tinta = cobertura/3
latas = float(litros_tinta/18)
print(latas)

if (litros_tinta/18) != (litros_tinta//18):
    latas = float(litros_tinta//18 + 1)


preco = float((latas*80))
print("quantidade de latas: " + str(int(latas)))
print(f"preço total: R${preco:,.2f}")
