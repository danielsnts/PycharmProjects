valor = float(input("Insira um valor para sacar"))

i = int()
nota = valor // 100
if nota == 0:
    i = 0
else:
    i = 1
print(f"{nota:,.0f} * R$ 100,00" *i)

valor -= nota * 100
nota = valor // 50
if nota == 0:
    i = 0
else:
    i = 1
print(f"{nota:,.0f} * R$ 50,00" *i)

valor -= nota * 50
nota = valor // 10
if nota == 0:
    i = 0
else:
    i = 1
print(f"{nota:,.0f} * R$ 10,00" *i)

valor -= nota * 10
nota = valor // 5
if nota == 0:
    i = 0
else:
    i = 1
print(f"{nota:,.0f} * R$ 5,00" *i)

valor -= nota * 5
nota = valor // 1
if nota == 0:
    i = 0
else:
    i = 1
print(f"{nota:,.0f} * R$ 1,00" *i)
