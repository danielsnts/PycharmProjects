peso = float(input("Inrira a=o peso dos peixes PESCADOS\n"))
excesso = peso - 50
multa = excesso*4
if excesso > 0:
    print("-----------------------")
    print(f"Pescado: {peso:,.2f}kg")
    print(f"Excesso: {excesso:,.2f}kg")
    print(f"Multa: R${multa:,.2f}")
