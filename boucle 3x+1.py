l = ["r","b"]


for i in range(6):
    x = []
    for i in range(len(l)):
        if l[i] == "b":
            x.append("r")
            x.append("b")
        elif l[i] == "r":
            x.append("b")
    l=x
    print(l)
