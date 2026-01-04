N = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

unique_sum = 0
for key in freq:
    if freq[key] == 1:
        unique_sum += key

print("Sum of elements appearing exactly once:", unique_sum)
