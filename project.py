ma = ["m", "pc", "h", "ses", "svt", "f", "s", "a", "emc", "all", "esp", "snt"]

print(""" bonjour toi
je te connais pas,
du moins, pas encore,
mon but sera d'essayer de deviner ton prénom et ton nom,
en trois question,
\nJe suis pour l'instant limité au 18 personne des immigrés,
mais je peux toujours m'améliorer au fil du temps """)

print(""" \nj'ai créé un code pour les matiéres pour pas que tu les tapes en entiere,
retient les biens, c'est important pour mon fonctionnement:\n """)

print("""math=m
physique=pc
histoire=h
ses=ses
svt=svt
francais=f
sport=s
anglais=a
emc=emc
allemand=all
espagnol=esp
snt=snt\n""")

while True:
	m1 = str(input("entre ta matiere préféré num1: "))
	
	if m1 in ma:

		if m1 == "m":
			m2 = str(input("okay, noté, donne moi ta seconde matiére préféré: "))
			
			if m2 == "ses":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "pc":
					print("\nTU ES CHLOE LOIRE!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Chloé"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")
			
			elif m2 == "h":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))

				if m3 == "f":
					print("\noulah j'ai un probléme")
					print("j'ai deux possibilité.")
					print("comment pourrais-je vous distinguer....")
					print("JE SAIS!!!")
					x = str(input("\ndonne la premiere lettre de ton prénom(en minuscule): "))
					
					if x == "z":
						print("\nTU ES ZOE CHRETIEN!!")
						y = str(input("\nVrai ou faux (v/f)? "))
					
						if y == "v":
							print("\nj'ai gagné!!\n")
							name = "Zoé"
							break
						
						else:
							print("\ndesolé, je ne sais pas qui tu es alors.")
							print("donne d'autres matiéres pour réessayer.\n")
						
					elif x == "h":
						print("\nTU ES HIPPOLYTE MAITROT!!")
						y = str(input("\nVrai ou faux (v/f)? "))
					
						if y == "v":
							print("\nj'ai gagné!!\n")
							name = "Hippolyte"
							break
						
						else:
							print("\ndesolé, je ne sais pas qui tu es alors.")
							print("donne d'autres matiéres pour réessayer.\n")
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")

				elif m3 == "svt":
					print("\nTU ES EUGENIE BAYLE!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Eugénie"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")

				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "pc":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))

				if m3 == "f":
					print("\nTU ES NOAM FAVIER, MON CREATEUR")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nc'est bien vous maitre, merci de m'avoir créé, j'ai hate d'avoir de nouvelle maj\n")
						name = "Maitre"
						break
					
					else:
						print("\ndésolé, je vous croyais être mon createur.")
						print("donne d'autres matiéres pour réessayer.\n")

				elif m3 == "snt":
					print("\nTU ES VICTOIRE LECLERC")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Victoire"
						break
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
					
				elif m3 == "emc":
					print("\nTU ES MAXENCE MARCAIRE")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Maxence"
						break
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")

				elif m3 == "s":
					print("\nTU ES LISA DELAROCHE-VERNET")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "lisa"
						break
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "ang":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))

				if m3 == "s":
					print("\nTU ES PHILIPPINE GUIZIOU!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Philippine"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")
			
			elif m2 == "snt":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "all":
					print("\nTU ES AMAURY PERRAULD!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Amaury"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			else:
				print("\ndésolé je ne connais pas quelqu\'un qui aime cette matiére")
		
		elif m1 == "h":
			m2 = str(input("okay, noté, donne moi ta seconde matiére préféré: "))

			if m2 == "m":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))

				if m3 == "f":
					print("\noulah j'ai un probléme")
					print("j'ai deux possibilité.")
					print("comment pourrais-je vous distinguer....")
					print("JE SAIS!!!")
					x = str(input("\ndonne la premiere lettre de ton prénom(en minuscule): "))
					
					if x == "z":
						print("\nTU ES ZOE CHRETIEN!!")
						y = str(input("\nVrai ou faux (v/f)? "))
					
						if y == "v":
							print("\nj'ai gagné!!")
							name = "Zoé"
							break
						
						else:
							print("\ndesolé, je ne sais pas qui tu es alors.")
							print("donne d'autres matiéres pour réessayer.\n")
						
					elif x == "h":
						print("\nTU ES HIPPOLYTE MAITROT!!")
						y = str(input("\nVrai ou faux (v/f)? "))
					
						if y == "v":
							print("\nj'ai gagné!!")
							name = "Hippolyte"
							break
						
						else:
							print("\ndesolé, je ne sais pas qui tu es alors.")
							print("donne d'autres matiéres pour réessayer.\n")
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")

				elif m3 == "svt":
					print("\nTU ES EUGENIE BAYLE!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!")
						name = "Eugénie"
						break
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")

				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")
			
			elif m2 == "ses":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "m":
					print("\nTU ES AUDE SIMON!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Aude"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "a":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "f":
					print("\nTU ES JOHANA GAYOSSO RIO DE LA LOZA!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Johana"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")				
				
			elif m2 == "s":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "m":
					print("\nTU ES ERWAN VIAUD!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Erwan"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			else:
				print("\ndésolé je ne connais pas quelqu\'un qui aime cette matiére")

		elif m1 == "ses":
			m2 = str(input("okay, noté, donne moi ta seconde matiére préféré: "))

			if m2 == "s":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "m":
					print("\nTU ES JULIEN BEAUMONT!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Julien"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")
			
			elif m2 == "m":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "pc":
					print("\nTU ES CHLOE LOIRE!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Chloé"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")
			
			elif m2 == "a":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "m":
					print("\nTU ES LENA MASSART!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Léna"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "h":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "m":
					print("\nTU ES AUDE SIMON!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Aude"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			else:
				print("\ndésolé je ne connais pas quelqu\'un qui aime cette matiére")
		
		elif m1 == "pc":
			m2 = str(input("okay, noté, donne moi ta seconde matiére préféré: "))

			if m2 == "s":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "f":
					print("\nTU ES THOMAS GENTE!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Thomas"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")
			
			elif m2 == "m":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))

				if m3 == "f":
					print("\nTU ES NOAM FAVIER, MON CREATEUR")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nc'est bien vous maitre, merci de m'avoir créé, j'ai hate d'avoir de nouvelle maj\n")
						name = "Maitre"
						break
					
					else:
						print("\ndésolé, je vous croyais être mon createur.")
						print("donne d'autres matiéres pour réessayer.\n")

				elif m3 == "snt":
					print("\nTU ES VICTOIRE LECLERC")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Victoire"
						break
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
					
				elif m3 == "emc":
					print("\nTU ES MAXENCE MARCAIRE")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Maxence"
						break
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")

				elif m3 == "s":
					print("\nTU ES LISA DELAROCHE-VERNET")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Lisa"
						break
						
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")

			else:
				print("\ndésolé je ne connais pas quelqu\'un qui aime cette matiére")

		elif m1 == "s":
			m2 = str(input("okay, noté, donne moi ta seconde matiére préféré: "))

			if m2 == "ses":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "m":
					print("\nTU ES JULIEN BEAUMONT!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Julien"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "esp":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "a":
					print("\nTU ES HIPPOLYTE CHARLES!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Hippolyte"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "pc":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "f":
					print("\nTU ES THOMAS GENTE!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Thomas"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "h":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "m":
					print("\nTU ES ERWAN VIAUD!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Erwan"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			else:
				print("\ndésolé je ne connais pas quelqu\'un qui aime cette matiére")

		elif m1 == "a":
			m2 = str(input("okay, noté, donne moi ta seconde matiére préféré: "))

			if m2 == "ses":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "m":
					print("\nTU ES LENA MASSART!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "m":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "s":
					print("\nTU ES PHILIPPINE GUIZIOU!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			elif m2 == "h":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "f":
					print("\nTU ES JOHANA GAYOSSO RIO DE LA LOZA!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")

			else:
				print("\ndésolé je ne connais pas quelqu\'un qui aime cette matiére")

		elif m1 == "esp":
			m2 = str(input("okay, noté, donne moi ta seconde matiére préféré: "))

			if m2 == "s":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "a":
					print("\nTU ES HIPPOLYTE CHARLES!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Hippolyte"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")
			
			else:
				print("\ndésolé je ne connais pas quelqu\'un qui aime cette matiére")
		
		elif m1 == "snt":
			m2 = str(input("okay, noté, donne moi ta seconde matiére préféré: "))
			
			if m2 == "m":
				print("\nje crois savoir qui tu es!")
				m3 = str(input("donne moi ta matiéres détésté pour verifier: "))
				
				if m3 == "all":
					print("\nTU ES AMAURY PERRAULD!!")
					y = str(input("\nVrai ou faux (v/f)? "))
					
					if y == "v":
						print("\nj'ai gagné!!\n")
						name = "Amaury"
						break
					
					else:
						print("\ndesolé, je ne sais pas qui tu es alors.")
						print("donne d'autres matiéres pour réessayer.\n")
				
				else:
					print("\ndesolé, je ne sais pas qui tu es.")
					print("donne d'autres matiéres pour réessayer.\n")
			
			else:
				print("\ndésolé je ne connais pas quelqu\'un qui aime cette matiére")

		else: 
			print("désolé je ne connais pas de personne qui aimes cette matiére")
	
	else:
		print("\ndesolé, mais je ne connais pas cette matiéres\n")

print("Okay", name)
print("maintenant que j'ai ton nom,")
print("on va aller plus loin.")
z = str(input("as tu besoin d'aide dans une matiéres?(o/n) "))

if z == "o":
	print("\nokay voyons voir qui peut t'aider.")
	m4 = str(input("donne moi la matiéres où tu as besoin d'aide: "))
	print("\nokay, tu peux demander de l'aide à:")

	if m4 == "m":
		print("Chloé, Hyppolyte M, Zoé, Eugénie, Noâm, victoire, maxence, lisa, amaury et philippine\n")

	elif m4 == "h":
		print("Aude, Erwan, Hippolyte M, Zoé, Eugénie, Johana\n")

	elif m4 == "ses":

		print("Julien, Chloé, Léna, Aude\n")

	elif m4 == "pc":
		print("Thomas, Noâm, Victoire, Lisa, Maxence\n")
	
	elif m4 == "s":
		print("Erwan, Julien, Hippolyte C, Thomas\n")

	elif m4 == "a":
		print("Léna, Philippine, Johana\n")

	elif m4 == "esp":
		print("Hippolyte C\n")
	
	elif m4 == "snt":
		print("Amaury\n")
	
	else:
		print("désolé, je connais pas de personne qui peuvent t'aider dans cette matiéres")

else:
	print("Okay",name,",passe une bonne journé")