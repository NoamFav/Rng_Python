from time import *

print("\nbonjour mon but est de vous donner les diviseurs d'un nombre")
sleep(2)
print("(mais bon, j'ai du mal avec les trop gros chiffres(5/6 chiffres max))")
sleep(2)

while True:
    x = int(input("\nchoisie ton nombre:  "))
    y = [i for i in range(1, x+1) if x % i == 0]
    print("\nprgm en cours...")
    sleep(1)
    print("\n", x, "est divisible par:\n ", y)
    if max(y) == x  and  min(y) == 1 and len(y) == 2:
        print(x, "est un nombre premier")
    elif x == 1:
        sleep(1)
        print(x, "est un nombre premier")
    sleep(1)
    print("\nveux tu continuer?")
    g = int(input("\noui ou non(1/0)\nou pgcd(2):"))
    if g == 1:
        sleep(1)
        print("\nrelancement du prgm...")
        sleep(1)

    elif g == 0:
        sleep(1)
        print("\nfin du pgrm...")
        sleep(1)
        break
    elif g==2:
        sleep(1)
        s=int(input("\nchiffre a comparer: "))
        u=[i for i in range(1, s+1) if s % i == 0]
        h=0
        for i in y:
            if i in u and i>h:
                h=i
        sleep(1)
        print("\nprgm en cours...")
        sleep(1)
        if h!=1:
            print("\nle pgcd entre",x,"et",s,"vaut:",h)
        else:
            print("\nil n'y a pas de pgcd")
        t = int(input("""Voulez vous continuer ?
oui ou non (1/0): """))
        if t == 1:
            sleep(1)
            print("\nrelancement du prgm...")
            sleep(1)
        elif t > 1:
            print("\nchoix non valide")
            sleep(1)
            print("relancement systeme...")
            sleep(1)
        elif t == 0:
            sleep(1)
            print("\nfin du pgrm...")
            sleep(1)
            break
