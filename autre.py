def pgcd(a,b):
    c = []
    for i in range(1,100001):
        c.append(i)
    d = []
    for i in c:
        if a % i == 0:
            d.append(i)
        else:
            continue
    e = []
    for i in c:
        if b % i == 0:
            e.append(i)
    h=0
    for i in d:
        if i in e and i>h:
            h=i
    return h


print(pgcd(215717,115))
            
