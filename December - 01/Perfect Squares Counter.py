N = int(input("Enter the number: "))
x = []
count = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j**2:
            x.append(i)
            count += 1
print(x)
print(count)
