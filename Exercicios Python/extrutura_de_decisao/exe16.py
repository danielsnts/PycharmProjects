a = float(input("A: \t"))
if a == 0:
    print("FIM")
else:
    b = float(input("B: \t"))
    c = float(input("C: \t"))

    delta = pow(b, 2) - 4 * a * c

    if delta < 0:
        print("Sem raízes reais")
    elif delta == 0:
        print(f"Solução : x = {-b/a}")
    else:
        x = (-b + pow(delta, 0.5))/(2*a)
        print(f"Solução 1: x1 = {x}")
        x = (-b - pow(delta, 0.5))/(2*a)
        print(f"Solução 2: x2 = {x}")
