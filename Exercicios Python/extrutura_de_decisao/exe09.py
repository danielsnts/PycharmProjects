vetor = [int(0),int(0),int(0),int(0)]
a = int(0)
for i in range(0,3):
    vetor[i] = int(input("Insira:\t"))

for i in range(0, 3):
    for j in range(0, 3):
        if vetor[i] < vetor[i+1]:
            a = vetor[i]
            vetor[i] = vetor[i+1]
            vetor[i+1] = a

for i in range(0,3):
    print(f"------------\n{vetor[i]}")