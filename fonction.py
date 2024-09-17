list1 = []
list3 = []
list4 = []

x = int(input("nombre de degré: "))

for i in range(0, x+1):
    list1.append(i)

list2=list1[::-1]

for i in list2:
    print("enter variable n°",i,": ")
    a=float(input())
    list3.append(a)

y= float(input("valeur de x: "))

for i in range(0,x+1):
    print(i)
    list4.append(list3[i]*(y**list2[i]))

print(list4)
print(sum(list4))
