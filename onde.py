from ti_system import *
from time import sleep

P = 0
h = 6.62607015*(10**(-34))
c = 299792458

while True:
    
    disp_clr()
    if P == 0:
        print("Bonjour je m'appelle Pc-Ti82 =)")
        print("que cherches-tu en moi? ;-)")
        print("""1. des formules?
2. des info (un peu de tout)?
3. des constantes?""")
        x = int(input("ton choix: "))
    
    elif P > 0:
        print("reprenons, voici t'es options:")
        print("""1. des formules
2. des info (un peu de tout)
3. des constantes""")
        x = int(input("que veux tu de plus: "))
    disp_clr()
    if x == 1:
        print("ok, quel formule?")
        y = int(input("""1. la frequence (f)
2. vitesse (v)
3. la longueur d'onde (lambda)
4. énergie (E)
5. vitesse moyenne (Vi)
6. somme des force (somme(F))
ton choix: """))
        disp_clr()
        if y == 1:
            print("pour rappel: f = 1/T")
            T = float(input("valeur de T (en s): "))
            print("f = ",1/T,"Hz")
        elif y == 2:
            print("pour rappel: v = lambda/T")
            L = float(input("valeur de lambda (en m): "))
            T = float(input("valeur de T (en s): "))
            print("v = ",L/T,"m/s")
        elif y == 3:
            print("quel donnée as-tu?")
            m = int(input("""1. T (et c)
2. nu (et c)
3. E (et h et c)
ton donnée: """))
            disp_clr()
            if m == 1:
                print("pour rappel: lambda = c*T")
                T = float(input("valeur de T (en s): "))
                print("lambda = ", c*T, "m")
            elif m == 2:
                print("pour rappel: lambda = c/nu")
                nu = float(input("valeur de nu (en Hz): "))
                print("lambda = ", c/nu,"m")
            elif m == 3:
                print("pour rappel: lambda = hc/E")
                E = float(input("valeur de E (en J): "))
                print("lambda = ", (h*c)/E,"m")
        elif y == 4:
            print("quel donnée as-tu?")
            B = int(input("""1. lambda (et h et c)
2. nu (et h)
ton choix: """))
            disp_clr()
            if B == 1:
                print("pour rappel: E = hc/lambda")
                l = float(input("valeur de lambda (en m): "))
                print("E = ", (h*c)/l, "J")
            elif B == 2:
                print("pour rappel: E = h*nu")
                nu = float(input("valeur de nu (en Hz): "))
                print("E = ", h*nu, "J")
        elif y == 5:
            print("pour rappel: Vi = (Mi-1 Mi+1)/2(delta(t))")
            d = float(input("distance entre Mi-1 et Mi+1 (en m): "))
            t = float(input("valeur de delta(t) (en s): "))
            print("Vi = ", d/(2*t), "m/s")
        elif y == 6:
            print("pour rappel: somme(F)= m(delta(V)/delta(T)")
            m = float(input("valeur de m (en kg): "))
            V = float(input("valeur de delta(V) (en m/s): "))
            t = float(input("valeur de delta(t) (en s): "))
            print("somme(F) = ", m*(V/t), "N")
    elif x == 2:
        print("ok, quel type info?")
        y = int(input("""1. onde mécanique
2. onde éléctromagnétique
3. vecteur vitesse
ton choix: """))
        disp_clr()
        if y == 1:
            print("que veux-tu savoir ;-)")
            z = int(input("""1. onde méca progressive
2. célérité v
3. T
4. f
5. lambda
ton choix: """))
            disp_clr()
            if z == 1:
                print("onde méca prog = propagation d'une perattubion sans trsp de matiere mais d'energie")
            elif z == 2:
                print("célérité v = vitesse de propagation de l'onde. d/delta(t)")
            elif z == 3:
                print("periode temporelle en s")
            elif z == 4:
                print("frequence en Hz")
            elif z == 5:
                print("distance parcourue par l'onde pendant une durée égale à sa période temporelle")
        elif y == 2:
            print("que veux-tu savoir ;-)")
            z = int(input("""1. onde
2. diagram d'energie
ton choix: """))
            disp_clr()
            if z == 1:
                print("""1m<lmbd<1000m: onde hertzienne
1mm<lmbd<1m: micro-ondes
800nm<lmbd<1mm: infraRouge
400nm<lmbd<800nm: onde visible 
10nm<lmbd<400nm: UV
0.001nm<lmbd<10nm: rayons X
lmbd <0.001nm : rayon gamma""")
            elif z == 2:
                print("""energie E exprimé en eV, =valeur possible d'un atome
etat fondamentale:  etat le plus bas
etat supérieur: état excité""")
        elif y == 3:
            print("que veux-tu savoir ;-)")
            z = int(input("""1. vitesse instantanée
2. vecteur vitesse instantanée
3. vecteur variation
4. principe de l'inertie
5. somme des forces
6. deuxieme loi de newton
ton choix: """))
            disp_clr()
            if z == 1:
                print("vitesse moyenne sur une tres courte durée")
            elif z == 2:
                print("Mi-1 et Mi+1 // delta(Vi)")
            elif z == 3:
                print("delta(Vi)= Vi+1 - Vi-1")
            elif z == 4:
                print("si var vecteur vitesse = 0: reciproque vrai")
            elif z == 5:
                print("""delta(Vi): direction/sens particulier
construction somme(F): delta(Vi) et somme(F)= same direction/sens""")
            elif z == 6:
                print("""somme(F) = m(delta(V)/delta(t))
m/delta(V)= sens,direc,resultante(F)
(delta(V)/delta(t)) est donc inversement proportionnel à m: (delta(V)/delta(t)) = (1/m)(somme(F)
P=mg donc 2eme loi Newton=
somme(F)=P or P=mg, donc:(delta(V)/delta(t))=(1/m)*somme(F) <=> (delta(V)/delta(t))=(1/m)*mg,d'où:(delta(V)/delta(t))=g""")
                sleep(5)
    if x == 3:
        print("ok quel constante?")
        y = int(input("""1. constante de Plancks
2. célérité de la vitesse de la lumiere
3. valeur d'1eV en J
ton choix: """))
        disp_clr()
        if y == 1:
            print("constante de planck (h) =      ", h, "J/Hz")
        elif y == 2:
            print("célérité de la lumiére (c) =   ", c, "m/s")
        elif y == 3:
            print("1eV =1.6 * (10**(-19) J")
    
    sleep(5)

    Y = int(input("""

as-tu besoin de quelque chose d'autre: 
1. OUI
2. NON
so? tu veux: """))
    disp_clr()
    if Y == 1:
        print("restart de mon interface...")
        sleep(1)
        P += 1
        continue
    elif Y == 2:
        print("j'espere t'avoir aider ;-)")
        print("peace out ;-)")
        break