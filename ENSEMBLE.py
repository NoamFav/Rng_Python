**TI83F*

Created by TI Connect CE 5.6.0.2082       � zENSEMBLE  zxPYCD print("choisie un type d'ensemble:")
print("1:[]")
print("2:[[")
print("3:]]")
print("4:][")
v=[1,2,3,4]

while True:
  w=int(input("1/2/3/4: "))
  if w in v:
    z=float(input("debut de l'ensemble: "))
    y=float(input("fin de l'ensemble: "))
    if z!=y and z<y:
      x=float(input("valeur a verifier: "))
      if w==1:
        if x<z:
          print("trop petit")
        elif x>y:
          print("trop grand")
        else:
          print("dans l'ensemble")
        break
      elif w==2:
        if x<z:
          print("trop petit")
        elif x>=y:
          print("trop grand")
        else:
          print("dans l'ensemble")
        break
      elif w==3:
        if x<=z:
          print("trop petit")
        elif x>y:
          print("trop grand")
        else:
          print("dans l'ensemble")
        break
      elif w==4:
        if x<=z:
          print("trop petit")
        elif x>=y:
          print("trop grand")
        else:
          print("dans l'ensemble")
        break
    else:
      print("ensemble incorect")
      print("reessai\n")
  else:
    print("nombre non reconnue")
    print("reessai\n")�5