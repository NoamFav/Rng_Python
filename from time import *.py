
sleep(1)
print("\nbonjour mon but est de vous donner les diviseurs d'un nombre")
sleep(2)
print("(mais bon, j'ai du mal avec les trop gros chiffres(5/6 chiffres max))")
sleep(2)
a = []

for i in range(1, 1001):
    a.append(i)
    


while True:
    while True:
        try:
            x = int(input("\nchoisie ton nombre:  "))
            if type(x) == int:
                break
        except ValueError:        
            print("\nerreur systeme")
            sleep(1)
            print("\nrelancement du pgrm...")
            sleep(1)
    y = []
    for i in a:
        if x % i == 0:
            y.append(i)
        else:
            continue
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
    while True:
        try:
            g = int(input("\noui ou non(1/0)\nou pgcd(2):"))
            if type(g)==int:
                break
        except ValueError:
            print("\nerreur systeme")
            sleep(1)
            print("\nrelancement du pgrm...")
            sleep(1)
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
        while True:
            try:
                s=int(input("\nchiffre a comparer: "))
                if type(s)==int:
                    break
            except ValueError:
                print("\nerreur systeme")
                sleep(1)
                print("\nrelancement du pgrm...")
                sleep(1)
        u=[]
        for i in a:
            if s % i == 0:
                u.append(i)
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
        while True:
                try:
                    t = int(input("""Voulez vous continuer ?
oui ou non (1/0): """))
                    if type(t)==int:
                        break
                except ValueError:

                    print("\nerreur systeme")
                    sleep(1)
                    print("\nrelancement du pgrm...")
                    sleep(1)
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
