from ti_system import *


disp_clr
print("quel deriver cherche tu?")
x = int(input("""1.fonction élémentaire
2. regle de derivation
3. trigo
votre choix: """))

disp_clr
if x == 1:
    print("""- f(x) = k ,R, f'(x) = 0
- f(x) = x ,R, f′(x) = 1
- f(x)= x^n, n E N*, R, f'(x)= nx^(n-1)
- f(x)= 1/x , R*, f'(x)= -1/(x^2)
- f(x)= 1/(x^n), R*, f'(x)= -n/(x^(n+1))
- f(x)= sqrt(x), R+, f'(x)= 1/(2sqrt(x))""")
elif x==2:
    print("""-deriver de la somme: (u+v)′ = u′+v′
-deriver de ku: (ku)′ = ku′
-deriver du produit: (uv)′ = u′v + uv′
-deriver de l'inverse: (1/u)' = -u'/u^2
-deriver du quotient: (u/v)' = (u'v-uv')/v^2
-deriver de la puissance: (u^n)' = nu'u^(n-1)
-deriver de la racine: (sqrt(u))' =  u'/(2sqrt(u))""")
elif x==3:
    print("deriver en cercle: sin -> cos -> -sin -> -cos")
