x = []

N = int(input("Enter the number of elements: "))
k = int(input("Enter the target sum: "))

for i in range(N):
    num = int(input("Enter the number: "))
    x.append(num)

start = 0
current_sum = 0
found = False

for end in range(N):
    current_sum += x[end]

    while current_sum > k and start <= end:
        current_sum -= x[start]
        start += 1

    if current_sum == k:
        print(start, end)
        found = True
        break

if not found:
    print(-1, -1)
