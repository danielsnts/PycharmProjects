participacao = int(0)
print("Telefonou para a vítima?\n")
resposta = int(input("1 = SIM\n2 = NÃO"))
if resposta == 1:
    participacao += 1

print("Esteve no local do crime?\n")
resposta = int(input("1 = SIM\n2 = NÃO"))
if resposta == 1:
    participacao += 1

print("Mora perto da vítima?\n")
resposta = int(input("1 = SIM\n2 = NÃO"))
if resposta == 1:
    participacao += 1

print("Devia para a vítima?\n")
resposta = int(input("1 = SIM\n2 = NÃO"))
if resposta == 1:
    participacao += 1

print("Já trabalhou com a vítima?\n")
resposta = int(input("1 = SIM\n2 = NÃO"))
if resposta == 1:
    participacao += 1

if participacao <= 2:
    print("SUSPEITO")
elif participacao <= 4:
    print("CÚMPLICE")
else:
    print("ASSASSINO")
