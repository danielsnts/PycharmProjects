lado1 = float(input("Insira o primeiro lado:\n"))
lado2 = float(input("Insira o segundo lado:\n"))
lado3 = float(input("Insira o terceiro lado:\n"))

cond1 = (lado1 + lado2 > lado3)
cond2 = (lado1 + lado3 > lado2)
cond3 = (lado3 + lado2 > lado1)

if cond1 and cond2 and cond3:
    print("É um triângulo!!")

    if lado1 == lado2 == lado3:
        print("Equilátero")
    elif (lado2 == lado1) or (lado3 == lado1) or (lado2 == lado3):
        print("Isósceles")
    else:
        print("Escaleno")
else: print("Não é um triângulo!!")