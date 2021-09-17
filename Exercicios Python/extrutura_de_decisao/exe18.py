data = str(input("Insira uma data (dd/mm/aaaa)"))

dd = int(data[0:2])
mm = int(data[3:5])
aaaa = int(data[6:11])

print(f"DATA {data} ... ANALIZANDO")

if dd > 29 and mm == 2:
    print("Inválido")
elif (dd == 29 and mm == 2) and aaaa % 4 != 0:
    print("Inválido")
elif dd == 31 and mm is not [1, 3, 5, 7, 8, 10, 13]:
    print("Inválido")
elif dd < 1:
    print("Inválido")
elif data[2] != "/" or data[5] != "/":
    print("Inválido")
else:
    print(f"Data {dd:02}/{mm:02}/{aaaa:04} VÁLIDA")
