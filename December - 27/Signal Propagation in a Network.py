import heapq

N = int(input())
M = int(input())

adj = [[] for _ in range(N)]

for _ in range(M):
    u, v, t = map(int, input().split())
    adj[u].append((v, t))

S = int(input())

INF = float('inf')
dist = [INF] * N
dist[S] = 0

pq = [(0, S)]

while pq:
    time, node = heapq.heappop(pq)

    if time > dist[node]:
        continue

    for nei, wt in adj[node]:
        if dist[nei] > time + wt:
            dist[nei] = time + wt
            heapq.heappush(pq, (dist[nei], nei))

ans = 0
for d in dist:
    if d == INF:
        print(-1)
        exit()
    ans = max(ans, d)

print(ans)
