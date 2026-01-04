from collections import deque

M, N = map(int, input().split())
maze = [list(input().strip()) for _ in range(M)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(M):
    for j in range(N):
        if maze[i][j] == 'S':
            start = (i, j)

visited = [[[False] * (1 << 10) for _ in range(N)] for _ in range(M)]

queue = deque()
queue.append((start[0], start[1], 0, 0)) 
visited[start[0]][start[1]][0] = True

while queue:
    x, y, keys, steps = queue.popleft()

    if maze[x][y] == 'T':
        print(steps)
        exit()

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < M and 0 <= ny < N:
            cell = maze[nx][ny]

            if cell == '#':
                continue

            new_keys = keys

            if 'a' <= cell <= 'j':
                new_keys |= (1 << (ord(cell) - ord('a')))

            if 'A' <= cell <= 'J':
                if not (keys & (1 << (ord(cell) - ord('A')))):
                    continue

            if not visited[nx][ny][new_keys]:
                visited[nx][ny][new_keys] = True
                queue.append((nx, ny, new_keys, steps + 1))

print(-1)
