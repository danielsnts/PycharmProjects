valor_hora = float(input("Insira o quanto voçê ganha por horas trabalhadas:\t"))
h_trabalhadas = float(input("Insira a quantidade de horas trabalhadas:\t"))

salario_bruto = (valor_hora*h_trabalhadas)
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
ir = salario_bruto*0.11
liquido = salario_bruto - inss -sindicato-ir
print(f"SALÁRIO BRUTO: R${salario_bruto:,.2f}")
print(f"IR (11%): R${ir:,.2f}")
print(f"INSS (8%): R${inss:,.2f}")
print(f"SINDICATO: R${sindicato:,.2f}")
print(f"SALÁRIO LÍQUIDO: R${liquido:,.2f}")