from time import sleep


def VA(x, y):
    return x-y


def coef_de_multi(x, y):
    return x/y


def pour_de_repart(x, y):
    return (x/y)*100


def to_de_var(x, y):
    return ((x-y)/y)*100


def id_de_var(x, y):
    return (x/y)*100


def id_de_repart(x, y):
    return x/y


def val_reel(x, y):
    return (x/y)*100


def val_nom(x, y):
    return (x/100) * y


def benef(x, y):
    return (x-y)


print("""que veux tu faire?
1.VA
2.coef de multiplicateur
3.% de repartition
4.taux de variations
5.indice de variations
6.indice de repartitions
7.valeur reel
8.valeurs nominales
9.benefices""")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sleep(1)

while True:
    b = int(input("ton choix: "))
    print(" ")
    if b in a:
        sleep(1)
        if b == 1:
            print("rappel: VA=CA-CI\n")
            c = float(input("valeurs une: "))
            d = float(input("valeurs deux: "))
            print("\nVA=", VA(c, d))
        elif b == 2:
            print("rappel: coef de multi=valeurs arivee/valeurs depart\n")
            c = float(input("valeurs une: "))
            d = float(input("valeurs deux: "))
            print("\ncoef de multi=", coef_de_multi(c, d))
        elif b == 3:
            print("rappel: % de repartition=(sous ensemble/ensemble)*100\n")
            c = float(input("valeurs une: "))
            d = float(input("valeurs deux: "))
            print("\n%_de_repartition=", pour_de_repart(c, d))
        elif b == 4:
            print("rappel: to de variations=((valeur arrive-valeur depart)/valeur depart)*100\n")
            c = float(input("valeurs une: "))
            d = float(input("valeurs deux: "))
            print("\nto de variation=", to_de_var(c, d))
        elif b == 5:
            print("rappel: indice de variation=(valeur arrive/valeur choisie comme base)*100\n")
            c = float(input("valeurs une: "))
            d = float(input("valeurs deux: "))
            print("\nindice de variation=", id_de_var(c, d))
        elif b == 6:
            print("rappel: indice de repartition=(valeurs etudie-valeurs choisie comme base)*100\n")
            c = float(input("valeurs une: "))
            d = float(input("valeurs deux: "))
            print("\nindice de repartition=", id_de_repart(c, d))
        elif b == 7:
            print("rappel: valeurs reel=(valeur nominal/indice des prix)*100\n")
            c = float(input("valeurs un: "))
            d = float(input("valeurs deux: "))
            print("\nvaleur reel=", val_reel(c, d))
        elif b == 8:
            print("rappel: valeur nominal=(valeurs reel/100)*indices des prix))\n")
            c = float(input("valeurs un: "))
            d = float(input("valeurs deux: "))
            print("\nvaleur nominal=", val_nom(c, d))
        elif b == 9:
            print("rappel: benefices=Chiffres affaires-consommation total")
            c = float(input("valeurs un: "))
            d = float(input("valeurs deux: "))
            print("benefices=", benef(c, d))
        break
    else:
        sleep(1)
        print("erreur systeme...")
        sleep(1)
        print("relancement du systeme...")
