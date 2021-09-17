nota = float(input("Insira a primera nota\t"))
nota2 = float(input("Insira a segunda nota\t"))
media = (nota + nota2) / 2

print(f"MEDIA: {media:,.2f}")
if media == 10:
    print("APROVADO COM DISTINÇÃO")
elif media >= 7:
    print("APROVADO")
else:
    print("REPROVADO")
