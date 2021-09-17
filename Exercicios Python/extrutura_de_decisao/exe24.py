num = float(input("Insira um numero: "))
print("1 par ou ímpar;\n2 positivo ou negativo;\n3 inteiro ou decimal.\n")
decisao = int(input("Insira a opcao:"))

if decisao == 1:
    if num % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
if decisao == 2:
    if num > 0:
        print("POSITIVO")
    else:
        print("NEGATIVO")
if decisao == 3:
    if num != round(num):
        print("DECIMAL")
    else:
        print("INTEIRO")
