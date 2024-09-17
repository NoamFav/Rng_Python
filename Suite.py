print("suite numérique")
x = int(input("""1. suite géo
2. suite arithmétique"""))

if x == 1:
    print("forme générale: Un = Up + (n-p)r")
    print("forme de recurence: Un+1 = un + r")
    print("Un+1 - Un constant")
    print("somme: Nombre de terme * (1er terme+ dernier terme)/2")
elif x == 2:
    print("forme générale: Un = Up + q**(n-p)")
    print("forme de recurrence: Vn+1 = q*Vn")
    print("(Vn+1)/Vn constant")
    print("nombre de terme * (q^nombre de terme - 1)/(q-1)")