vetor = list()

for i in range(10):
    a = int(input("Insira :\t"))
    vetor.append(a)
aux = int()
for i in range(10):
    for a in range(10-i-1):
        if vetor[a] > vetor[a+1]:
            aux = vetor[a]
            vetor[a] = vetor[a + 1]
            vetor[a+1] = aux
print(f"LISTA: {vetor}")
