notas = list()
soma = float(0)
for i in range(5):
    a = float(input(f"Nota {1+i}:\t"))
    notas.append(a)
    soma += notas[i]

print(f"Notas: {notas}")
print(f"Média: {soma/5}")