morango = float(input("Quantidade de morango (kg):\t"))
maca = float(input("Quantidade de maçã (kg):\t"))
if morango > 5:
    preco_morango = morango*2.2
else:
    preco_morango = morango*2.5

if maca > 5:
    preco_maca = maca*1.5
else:
    preco_maca = maca*1.8

preco_total = preco_maca + preco_morango
if preco_total >  25 or (morango + maca) > 8:
    preco_total *= 0.9
print(f"PREÇO TOTAL: R$ {preco_total:,.2f}")
