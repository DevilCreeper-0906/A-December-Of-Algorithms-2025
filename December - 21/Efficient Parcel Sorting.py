N = int(input())
queue = list(map(int, input().split()))

sorted_output = []

while queue:
    min_val = min(queue)
    min_index = queue.index(min_val)

    for _ in range(min_index):
        queue.append(queue.pop(0))

    sorted_output.append(queue.pop(0))

print(*sorted_output)
