print("formule a connaitre:")
print("""1. formule tangente
2. milieu droite
3. distance entre 2 point
4. calculer vecteur 2 point
5. équation de cercle
6. equation droite""")
x : int(input("choix: "))

if x == 1:
    print("Y=f(a)+f'(a)(x-a)")
elif x == 2:
    print("(xa-xa)/2")
    print("(ya-yb)/2")
elif x == 3:
    print("sqrt((xb-xa)**2+(yb-ya)**2)")
elif x == 4:
    print("xb-xa   yb-ya")
elif x == 5:
    print("C: (x-xa)**2+(y-ya)**2=R**2")
elif x == 6:
    print("ax + by + c = 0")