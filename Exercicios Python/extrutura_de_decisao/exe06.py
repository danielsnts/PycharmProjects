num1 = float(input("Insira o primero número\t"))
num2 = float(input("Insira o segundo número\t"))
num3 = float(input("Insira o terceiro número\t"))

maior = num1
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print("Maior : {}".format(maior))
print("Menor :{}".format(menor))