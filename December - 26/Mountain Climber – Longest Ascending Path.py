import sys
sys.setrecursionlimit(10**7)

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    max_len = 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] > grid[x][y]:
            max_len = max(max_len, 1 + dfs(nx, ny))

    dp[x][y] = max_len
    return max_len


answer = 0
for i in range(M):
    for j in range(N):
        answer = max(answer, dfs(i, j))

print(answer)
