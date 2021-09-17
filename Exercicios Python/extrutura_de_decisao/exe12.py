salario_bruto = float(input("INSIRA O SALÁRIO:\t"))
desconto = float(5)
INSS = float(0.1)
FGTS = float(0.11)

if salario_bruto <= 900:
    desconto = 0
elif salario_bruto <= 1500:
    desconto = 5
elif salario_bruto <= 2500:
    desconto = 10
else:
    desconto = 20

print(f"Salário Bruto: R$ {salario_bruto:,.2f}")
print(f"(-) IR ({desconto}%): R$ {(salario_bruto*desconto/100):,.2f}")
print(f"(-) INSS (10%): R$ {(salario_bruto*0.1):,.2f}")
print(f"FGTS (11%): R$ {(salario_bruto*0.11):,.2f}")
print(f"Total de Descontos : R$ {(salario_bruto*desconto/100) + (salario_bruto*0.1):,.2f}")

salario_liquido = salario_bruto - ((salario_bruto*desconto/100) + (salario_bruto*0.1))
print(f"Salário Líquido: R$ {salario_liquido:,.2f}")

