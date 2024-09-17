def cano(a, b, c):
    print("f(X)=",a,"X**2+",b,"X+",c)
    print("donc on a: ")
    delta=(b**2)-4*a*c
    d=4*a
    e=2*a
    print("f(X)=",a,"(X+",b,"/",e,")**2","-",delta,"/",d)
    if (b/e)%1 == 0 and (delta/d)%1 == 0:
        print("f(X)=",a,"(X","+",b/e,")**2","-",delta/d)
    elif (b/e)%1 != 0 and (delta/d)%1 == 0:
        print("f(X)=",a,"(X","+",b,"/",e,")**2","-",delta/d)
    elif (b/e)%1==0 and (delta/d)%1!=0:
        print("f(X)=",a,"(X","+",b/e,")**2","-",delta,"/",d)
    else:
        print("")
    return 'done'

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
print(cano(a,b,c))