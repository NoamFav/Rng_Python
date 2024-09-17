print("quel radian vous intéresse: ")
x = int(input("""1. pi/6 et 7pi/6
2. pi/4 et 5pi/4
3. pi/3 et  4pi/3
4. 2pi/3 et 5pi/3
5. 3pi/4 et 7pi/4
6. 5pi/6 et 11pi/6
votre choix: """))

print("rappel: axe x= cosinus et axe y= sinus")
if x == 1:
    print("""co de pi/6: (sqrt(3)/2; 1/2) angle: 30°
co de 7pi/6: (-sqrt(3)/2; -1/2) angle: 210°""")
elif x == 2:
    print("""co de pi/4: (srqrt(2)/2; sqrt(2)/2) angle: 45°
co de 5pi/4: (-sqrt(2)/2; -sqrt(2)/2) angle: 225°""")
elif x == 3:
    print("""co de pi/3: (1/2; sqrt(3)/2) angle: 60°
co de 4pi/3: (-1/2; -sqrt(3)/2) angle: 240°""")
elif x == 4:
    print("""co de 2pi/3: (-1/2; sqrt(3)/2) angle: 120°
co de 5pi/3: (1/2; -sqrt(3)/2) angle: 300°""")
elif x == 5:
    print("""co de 3pi/4: (-sqrt(2)/2; sqrt(2)/2) angle: 135°
co de 7pi/4: (sqrt(2)/2; -sqrt(2)/2) angle: 315°""")
elif x == 6:
    print("""co de 5pi/6: (-sqrt(3)/2; 1/2) angle: 150°
co de 11pi/6: (sqrt(3)/2; -1/2) angle: 330°""")
