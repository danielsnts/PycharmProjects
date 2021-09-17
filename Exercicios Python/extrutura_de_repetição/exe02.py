login = str(input("LOGIN: "))
password = str(input("SENHA: "))
while password == login:
    print("A SENHA NÃO PODE SER IGUAL AO USUÁRIO!!!\n")
    password = str(input("SENHA: "))
print("FIM")