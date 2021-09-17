cobertura = float(input("Insira a medida a ser pintada em m^2\:\t" ))
litros_tinta: float = cobertura/3
latas18 = float(litros_tinta//18)
print(latas18)

latas3_6 = (litros_tinta - latas18 * 18)/3.6

if ((litros_tinta - latas18 * 18)/3.6) != ((litros_tinta - latas18 * 18)//3.6):
    atas3_6 = (litros_tinta - latas18 * 18)//3.6 + 1


preco = float((latas18*80)+(latas3_6*25))
print("quantidade de latas (18L): " + str(int(latas18)))
print("quantidade de latas (3.6L): " + str(int(latas3_6)))
print(f"preço total: R${preco:,.2f}")
