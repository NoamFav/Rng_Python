x = int(input("""1-incertitude
2-onde
3-diffraction
4-interference
your choice:"""))

if x == 1:
    print("u(x)=s/sqrt(n)")
    print("z=|x-xref|/2")
    print("u=grad/2")
elif x== 2:
    print("v(célérité (m/s))=lmbd/T(s)=lmbd*f")
    print("f=1/T(s)")
    print("I=P(w)/s(m**2)")
    print("L(dB)=10*log(I(w/m**2/I0(1E-12w/m**2)")
    print("A(attenuation)=L1-L2=10*log(I1/I2)")
elif x == 3:
    print("angle de diffraction(rad) = L(m)/2D(m)")
    print("// (rad)=lmbd(m)/a(m)")
elif x == 4:
    print("dif de marche =  D2-D1  (tout en m)")
    print("// (constructive)= K(int)*lmbd")
    print("// (destructive) = (2K+1)*(lmbd/2)")
    print("i(interfrange)= (lmbd*D)/A(1-2)  (tt en m)")