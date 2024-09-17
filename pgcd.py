import time

def diviseur(x):
    y = []
    for i in range(1, x+1):
        if x % i == 0:
            y.append(i)
    return y

def pgcd(x, s):
    y = diviseur(x)
    u = diviseur(s)
    h = 0
    for i in range(len(y)):
        if u.count(y[i]) > 0 and y[i] > h:
            h = y[i]
    return h
