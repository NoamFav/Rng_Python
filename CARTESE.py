def point ():
    xa = float(input("xa = "))
    ya = float(input("ya = "))
    xb = float(input("xb = "))
    yb = float(input("yb = "))
    
    a=yb-ya
    b=-(xb-xa)
    c=-(a*xa+b*ya)
    
    print(a,"X+",b,"y+",c,"=0")
    print("le v directeur est: ",-b,"/",a)
    print("le v normal est: ",a,"/",b)


def vd ():
    xa = float(input("xa = "))
    ya = float(input("ya = "))
    v1 = float(input("chiffre du haut: "))
    v2 = float(input("chiffre du bas: "))

    a = v2
    b = -v1
    c = -(a*xa+b*ya)

    print(a,"X+",b,"y+",c,"=0")
    print("le v directeur est: ",-b,"/",a)
    print("le v normal est: ",a,"/",b)


def c_d ():
    xa = float(input("valeur de xa = "))
    ya = float(input("valeur de ya = "))
    cd = float(input("coef directeur = "))

    k = -(cd*xa)+ya
    print(cd,"x-y+",k,"=0")
    print("le v directeur est: ",-1,"/",cd)
    print("le v normal est: ",cd,"/",1)


print("""quel methode pour trouver equation cartesienne:
1- avec 2 points
2- avec 1 point et un vd
3- avec 1 point et un coef directeur""")
Z = int(input("choix: "))

if Z==1:
    point()
elif Z==2:
    vd()
elif Z==3:
    c_d()
else:
    print("erreur")