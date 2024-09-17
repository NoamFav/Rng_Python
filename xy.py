x = []
y = 0
for i in range(1,1000):
    for a in range(1,1000):
        if a**i < i**a:
            print("here is a solution, x = ",a,"and y = ",i)
            y+=1
print(y)