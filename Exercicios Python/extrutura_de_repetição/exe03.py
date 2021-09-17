

nome = str(input("Insira um nome -->\t"))
while len(nome) <= 3:
    nome = str(input("Insira um nome -->\t"))

idade = int(input("Insira a idade\t"))
while (idade < 0) or (idade > 150):
    idade = int(input("Insira a idade\t"))

salario = int(input("Insira o salrio\t"))
while salario < 0:
    salario = int(input("Insira o salrio\t"))

sexo = str(input("Insira o sexo\t"))
while sexo.lower() != "f" and sexo != "m":
    sexo = str(input("Insira o sexo\t"))

estado_c = str(input("Insira o estado civil\t"))
while not estado_c.lower() in ['s', 'd', 'v', 'c']:
    estado_c = str(input("Insira o estado civil\t"))
