from ti_system import *

disp_clr()
print("quel symetrie nécessaire")
x = int(input("""1. -a
2. pi-a
3. pi+a
4. (pi/2)-a
5. (pi/2)+a
votre choix: """))

disp_clr()
if x == 1:
    print("cos(-a)=cos(a); sin(-a)= -sin(a)")
elif x == 2:
    print("cos(pi-a)=-cos(a); sin(pi-a)= sin(a)")
elif x ==  3:
    print("cos(pi+a)=-cos(a); sin(pi+a)= -sin(a)")
elif x == 4:
    print("cos((pi/2)-a)= sin(a); sin((pi/2)-a)= cos(a)")
elif x == 5:
        print("cos((pi/2)+a)= -sin(a); sin((pi/2)+a)= cos(a)")

