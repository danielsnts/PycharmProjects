salario = float(input("INSIRA O SALÁRIO:\t"))

aumento = 0.25
if salario <= 280:
    aumento -= 0.05
elif salario <= 700:
    aumento -= 0.1
elif salario <= 1500:
    aumento -= 0.15
else:
    aumento -= 0.20

print(f"Salário: R$ {salario:,.2f}")
print(f"Percentual do aumento: {(aumento*100):,.2f}%")
print(f"Aumento: R$ {salario*aumento:,.2f}")
print(f"Novo Salário: R$ {(salario*(1+aumento)):,.2f}")
