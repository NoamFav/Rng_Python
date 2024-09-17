x = int(input("""1. constante
2. formule
3. definition
ton choix: """))

if x == 1:
    print("""constante:
G=6,67E-11 m3.kg-1.S-2 ou(en N.m2. kg-2)
g = 9,81N.kg-1 
k= 9,0. 109 N.m2. C-2""")
elif x == 2:
    print("Fg = mGr  (Gr = g sur terre")
    print("F(a/b) = F(b/a) = G(MaMb)/r**2")
    print("F(a/b)-> = G(Ma*Mb)/r**2 *u->")
    print("Fe = q E")
    print("loi de columb: Fe = k(Q/(d²))u")
    print("E = k(Q/(d²))u")
    print("Ec = 1/2 * m * v (v en m/s)")
    print("Epp = m * g * z (z en m)")
    print("Em = Ep + Ec")
    print("EPSI W(A->B)(F->) = delEc = EcB - EcA")
    print("W(AB)(P) = -Del*EppAB")
    print("DelEm = EPSI W AB (f-> non conservatrice)")
elif x == 3:
    print()