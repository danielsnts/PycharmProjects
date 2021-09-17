numero = str(input("Insira um número < 1000"))

if int(numero[0]) <= 1:
    print("1 unidade de milhar"*int(numero[0]), end="")
else:
    print(f"{numero[0]} unidades de milhar", end="")

if int(numero[1]) <= 1:# centenas
    print(", 1 centena, "*int(numero[1]), end="")
else:
    print(f", {numero[1]} centenas", end="")

if int(numero[2]) <= 1:#dezenas
    print(", 1 dezena"*int(numero[2]), end="")
else:
    print(f", {numero[2]} dezenas", end="")

if int(numero[3]) <= 1: #unidades
    print(" e 1 unidade"*int(numero[3]), end="")
else:
    print(f" e {numero[3]} unidades", end="")


