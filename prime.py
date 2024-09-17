def isPrime(num):
        if num > 2 and num % 2 == 0:
            return False, num
        for x in range(2, num // 2):
            if num % x == 0:
                return False, num
        return True, num
  
R = int(input("n ieme nombre premier:"))
A=[]
c=2

while len(A)<R:
    a,b=isPrime(c)
    if a: A.append(b)
    c+=1
print(A[-1])