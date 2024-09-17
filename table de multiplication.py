import random as rdm
from random import *

setup = ["*", "/"]
solu = 0
fail = 0
total = 0
n = str(input("quel mode veut tu? normal(n) ou extreme(x): "))
if n == "x":
    print("bonne chance champion;)")
else:
    del setup[1]
    print("bonne chance")

while True:
    n1 = randrange(2,10)
    n2 = randrange(2,10)
    ad = rdm.choice(setup)

    if n == "x":
        if ad == setup[1]:
            n1 = randrange(2,100)
            n2 = randrange(2,10)

    print(n1,ad, n2)
    while True:
        try:
            num = float(input("reponse: "))
            num / 1
            break
        except:
            print("nombre non valable")

    if num == 0:
        break
    if num == n1*n2 or num == n1/n2:
        solu += 1
    else:
        while num != n1*n2 or num == n1/n2:
            print("\nwrong")
            fail += 1
            print(n1, ad, n2)
            num = int(input("essaye a nouveau: "))
            if num == 0:
                break

    total += 1
    if fail + solu > total:
        solu -= 1

    pourc = (solu/total)*100
    print("\ntu as reussi ", pourc, "%' des reponses")
