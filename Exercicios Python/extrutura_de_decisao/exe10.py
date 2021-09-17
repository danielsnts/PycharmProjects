turno = str(input("Insira o turno em que você estuda: (M = MATUTINO,V = VESPERTINO,N = NOITE"))

if turno[0].upper() == "M":
    print("BOM DIA!")
elif turno[0].upper() == "V":
    print("BOA TARDE!")
elif turno[0].upper() == "N":
    print("BOA NOITE!")

