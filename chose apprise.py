# base de python:
# les formules de base a connaitre par coeur (et encore c un faible mots)
# (je passe toutes les opérations de base, je considére sa comme acquie de base)
print("je suis quelqu'un")  # on utilise "" ou '' pour definir une zone de texte
print(24//3)  # crée une division euclidienne
print(67 % 3)  # donne le reste d'une division euclidienne
print(45**2)  # factorielle (la: 45 puissance de 2)
print(float(2))  # force la machine a transformé 2 en un decimal flottant 2.0
print(str(2))  # transforme 2 en un caractére '2'
print("""ceci
est
en
plusieur
ligne""")  # on utilise """ pour annuler le fait de fermer un texte quand on change de ligne

print("j'ai 15ans"*2)  # multiplie une suite de caractére, regarder le resultat dans la console pour comprendre mieux

# donné une valeur a une variable:
# pour donner une valeur a une variale (le nom n'importe pas sauf, si il est égal a un nom protégé: if; print;etc..)
x = 34  # defini x
print('x', '=', x)  # rendu dans la console pour la lecture (pas nécessaire)

print(input('choisie un nom: '))  # demande a l'utilisateur de choisir un nombre. si 'input' est devant un: int;float;str;bool. cela définira le format de l'entrée a utilisé
# ex:
print(int(input('choisie un nombre: ')))

print('(x+=4)', '=', '(x=x+4)')  # on peut racourcir des opérations si on définit une nouvelle valeur d'une variable

# boolean:

# les boolean (ou bool) sont des types de caractére dont la réponse est seulement vrai ou faux (True ou False)

# comparaison:

# pour comparer des nombres on utilise: == (compare deux nombre et dit si il sont égaux),!= (compare deux nombre et donne l'ineverse'==',<,>,>=,<= (sa vous connaissez)

print(2 == 3)  # le resultat sera 'False'
print(2 != 3)  # le resultat sera 'False'
print(3 < 4)  # le resultat sera 'True'
print('hello' == 'hello')  # le resultat sera 'True'

# on peut aussi dire vrai si le resultat n'est pas bon, en utilisant la commande:
print(not 2 != 3)

# comparer deux boolean:

# and: permet de verifier si plusieur comparaison sont bonne (si une des comparaisons est fausse le resultat sera faux)
print(7 == 2 and 6 != 2)  # False

# or: permet de verifier si une des comparaisons est bonne (si plusieurs sont bonne le résulta sera tout de même vrai)
print(4 != 0 or 45 < 23)  # True

# on utilise '\' pour soit changer de ligne sur une meme formule (\n) ou pour utiliser une apostrophe sans fermer la zone de texte (\')

# if:
# crée une séquence seulement si les conditions sont réspécté

# else:
# crée une sequence si les variables de 'if' ne sont pas réspecté, mais ne crée pas une condition car il englobe juste le reste (else n'est jamais son if)

# elif:
# il suit if, et représente une fusion entre if et else (si if n'est pas respécté, il crée une autre conditions etc)

# ex:
# le programme si dessous défini si un nombre entrée (x) est pair ou impair
x = int(input('choisie une valeur de x: '))
if x % 2 == 0:  # défini si x est pair
	print('pair')
else:
	print('impair')

#boolean logic
#comme en math il y a un ordre pour effectuer les opérations
# la fonction '==' est prioritaire par rapport a 'and' et 'or'
print(3 == 3 and 6 != 7)
print(3 == 67 or 37 >= 23)

# base des listes:
# les listes sont des suite, soit de lettres, de chiffres, ou de mots
nums = [6, 7, 9, 4, 0, 3, 1]  # syntaxe d'une liste

print(nums[2])  # les index des listes commence a 0 et non à 1
print(nums + [3, 9, 0])  # ajoute des caractére a une liste
print(6 in nums)  # regarde si x est dans la liste

# fonction for list
print("nums.insert")  # inserer nbr
print("nums.append")  # ajouter nbr aprés
print("len(nums)")  # donner la taille d'une liste
print("max(nums)")  # donner la valeur la plus haute
print("min(nums)")  # donner nombres minimum
print("nums.count(x)")  # compte le nombre de fois que un caractére apparait
print("nums.remove(x)")  # enleve un nombre
print("nums.reverse(x)")  # inverse la liste

# while loops:
# les boucles "while" permet de répéter des block en boucles, et permet donc de créé pas mal de chose à la scratch

# le code ci dessous affiche tout le nombre qui sont inférieur ou égal à 5
i = 1
while i <= 5:
    print(i)
    i = i + 1  # à chaque tour du programme 1 est ajouté à i
print("Finished!")

# on utilise deux formule dans une boucle pour la rendre plus maniable: 
# 'break' qui ferme la boucle dés que il est Lu
# 'continue' qui ne lie pas une donné si variable respecté

# ex: le code ci dessous additionne tout les nombres pair de la liste
items = [23, 555, 666, 123, 128, 4242, 990]
sum = 0 	# variable de la somme
n = 0		# defini une variable pour stoper la boucle a un certain moment
while n < len(items): 	# permet de stopper la boucle a la fin de la liste
    num = items[n] 	# num defini le nombre a verifier par raport a son index representer par 'n'
    n = n + 1 	# prépare le second tour de boucle
    if num % 2 != 0: 	# verifie si nombre est impair
        continue  # ne li pas la donné si le nombre est impaire
    sum = sum + num 	# ajoute donc les nombres qui passe la formule if
print(sum) 	# écrit le résultat

# for loops
# La boucle for est utilisée pour itérer sur une séquence donnée, telle que des listes ou des chaînes de caractères.
# ce qu'il y a écrit aprés le 'for' prend la valeur du premier caractére en premier, puis le deuxiéme, etc... (dans le cas ci dessous word prend la valeur de 'lol', puis de 'jojo', etc...

# Le programme ci dessous rajoute un '!' aprés chaque mots
words = ['lol', 'jojo', 'lmao', 'youpi']
for word in words:
	print(word+'!')

# ex: le code ci dessous permet de compter le nombre de caractére identique dans une liste
letters = 'hello word'  # chaine de caractére à etudier
n = 0  # variables qui donnera le nombre de lettre
l = str(input("lettres à compter: "))

for x in letters:
	if x == l:
		n += 1  # si x = l, alors on rajoute un à n
print('il y a', n, l, 'dans letters')

# dif entre for et while:
# while: on l'utilise plus pour créé des boucles avec des donné inconnue
# for: souvent utilisé avec des listes fixé
# for est plus souvent utilisé car plus compact

# range:
# range permet de donner tout les nombres compris entre deux borne dans une liste
print(list(range(0, 20)))
# noter que il ne donnera pas la derniére valeur

# on peut aussi comparer deux listes
print(range(20) == range(0, 20))  # True

# on peut avoir un troisiéme argument qui permet de définir l'intervalle a chaque étape
print(list(range(0, 10, 2)))

# on peut combiner les boucles "for" et "range" en le mettant aprés le 'in' (comme sa pas besoin d'une liste prédéfini si c des suites logiques)
for i in range(5):
	print('hello!')

#important!!! a chaque fin de la formule if; else; elif; for, (avec conditions), il est obligatoire mettre':' sinon python affichera une erreur


# si vous voulez vous entrainez SoloLearn marche trés bien mêmes si payant

# et voila un exercice que vous pouvez essayer si vous voulez et envoyer moi votre réponse

# FizzBuzz est une mission de programmation bien connue, demandée lors d'interviews.

# Le code donné résout le problème de FizzBuzz et utilise les mots "Solo" et "Learn" au lieu de "Fizz" et "Buzz".
# Il prend une entrée n et sort les chiffres de 1 à n.
# Pour chaque multiple de 3, il imprime "Solo" au lieu du nombre.
# Pour chaque multiple de 5, il affiche "Learn" au lieu du nombre.
# Pour les nombres qui sont des multiples de 3 et 5, affichez "SoloLearn".
# Tout les nombre pair ne doivent pas aparaitre
