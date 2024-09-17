print("""1) nbr d'avogadro
2) m
3) C
4) Cm
5) n
6) v
7) pX (Cmere/Cfille/Vfille/Vmere
8) Cfille2
9) nbr molecule
10) masse vol
11) rappel des car""")
Na=6.022*(10**23)
a=int(input("que cherche tu? "))
print("\n")
if a==1:
    print("Na=6.022e23")
elif a==2:
  print("m=n*M or C*v*M")
  X=int(input("forme 1 ou 2: "))
  if X==1:
    n=float(input("valeur de n: "))
    M=float(input("valeur de M: "))
    print("m=",n*M)
  elif X==2:
    C=float(input("valeur de C: "))
    v=float(input("valeur de v: "))
    M=float(input("valeur de M: "))
    print("m=",C*v*M)
elif a==3:
  print("C=n/v or Cm/M")
  X=int(input("forme 1 ou 2: "))
  if X==1:
    n=float(input("valeur de n: "))
    v=float(input("valeur de v: "))
    print("v=",n/v)
  elif X==2:
    Cm=float(input("valeur de Cm: "))
    M=float(input("valeur de M: "))
    print("v=", Cm*M)
elif a==4:
  print("Cm=m/v or C*M")
  X=int(input("forme 1 ou 2"))
  if X==1:
    m=float(input("valeur de m: "))
    v=float(input("valeur de v: "))
    print("Cm=",m/v)
  elif X==2:
    C=float(input("valeur de C: "))
    M=float(input("valeur de M: "))
    print("Cm=", C*M)
elif a==5:
  print("n=m/M or C*v or n=pV/M or n=(Cm*V)/M")
  X=int(input("forme 1, 2, 3 ou 4"))
  if X==1:
    m=float(input("valeur de m: "))
    M=float(input("valeur de M: "))
    print("n=",m/M)
  elif X==2:
    C=float(input("valeur de C: "))
    v=float(input("valeur de v: "))
    print("n=",C*v)
  elif X==3:
    pV=float(input("valeur de pV: "))
    M=float(input("valeur de M: "))
    print("n= ", pV/M)
  elif X==4:
    Cm=float(input("valeur de Cm: "))
    V=float(input("valeur de V: "))
    M=float(input("valeur de M: "))
    print("n=",(Cm*V)/M)
elif a==6:
  print("v=m/rho")
  m=float(input("valeur de m: "))
  rho=float(input("valeur de rho: "))
  print("v=",m*rho)
elif a==7:
  print("Cmere/Cfille = Vfille/Vmere")
elif a==8:
  print("Cfille2=(Cfille1*Vmere2)/Vmere1")
elif a==9:
  print("nb molecule=n*Na")
  n=float(input("valeur de n: "))
  print("nb molecule=", n*Na)
elif a==10:
  print("rho=m/v")
  m=float(input("valeur de m: "))
  v=float(input("valeur de v: "))
  print("rho=",m/v)
elif a==11:
  print("""M=masse molaire(g/mol)
m=masse(g)
n=nbr mol(mol)
C=concentration(mol/L)
V=volume(L)
Cm=concentration massique(g/L)
rho=masse vol(g/cm**3 or kg/m**3""")
