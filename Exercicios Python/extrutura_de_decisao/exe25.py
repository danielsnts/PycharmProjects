combustivel = str(input("COMBUSTIVEL (A-álcool, G-gasolina):\t"))
litros = float(input("LITROS VENDIDOS:\t"))

if combustivel.upper() == "A":
    if litros <= 20:
        print(f"VALOR A SER PAGO: R$ {(litros*1.9*0.97):,.2f}")
    else:
        print(f"VALOR A SER PAGO: R$ {(litros*1.9*0.95):,.2f}")

if combustivel.upper() == "G":
    if litros <= 20:
        print(f"VALOR A SER PAGO: R$ {(litros*2.5*0.96):,.2f}")
    else:
        print(f"VALOR A SER PAGO: R$ {(litros*2.5*0.94):,.2f}")
