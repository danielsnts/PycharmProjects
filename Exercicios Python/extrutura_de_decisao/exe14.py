nota1 = float(input("Insira a primeira nota:\t"))
nota2 = float(input("Insira a segunda nota:\t"))

media = (nota1 + nota2)/2
print(f" Média de Aproveitamento : {media:,.2f}")
if media >= 9:
    print("Conceito A")
    print("APROVADO")
elif media >= 7.5:
    print("Conceito B")
    print("APROVADO")
elif media >= 6:
    print("Conceito C")
    print("APROVADO")
elif media >= 4:
    print("Conceito D")
    print("REPROVADO")
else:
    print("Seu merda!!!!")

    print("REPROVADO")
