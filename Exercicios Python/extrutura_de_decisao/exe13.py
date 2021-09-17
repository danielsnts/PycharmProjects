semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

num = int(input("Insira um numero"))

if num in range(0,8):
    print(f"{semana[num-1]}")
else:
    print("Número Inválido")