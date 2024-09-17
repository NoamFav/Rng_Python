from random import randint

x = randint(0, 100)
print("trouve le nombre caché entre O et 100")
essai = int(input("combien d'erreur possible autorise-tu?: "))

while True:
    n = int(input("\nton essaie: "))
    if n == x:
        print("Gagné!!")
        break
    elif n < x:
        print("\nessaie encore,\nindice: le nombre est plus grand")
        essai -= 1
        if essai == 0:
            print("Perdu!!!")
        print("essaie restant: ", essai)
    elif n > x:
        print("\nessaie encore,\nindice: le nombres est plus petit")
        essai -= 1
        if essai == 0:
            print("Perdu!!!")
        print("essaie restant: ", essai)
