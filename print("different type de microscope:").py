from ti_system *

disp_clr()
print("different type de microscope:")
print("""1.élec a balayage
2.a effet tunnel
3.a force atomique
4.optique de Hooke
5.elec à transmissions
6.optique de von Leevwenhoek""")
x= int(input("choose: "))

if x == 1:
    print("1935")
elif x == 2:
    print("1981")
elif x == 3:
    print("1986")
elif x== 4:
    print("1645")
elif x == 5:
    print("1931")
elif x == 6:
    print("1671")
