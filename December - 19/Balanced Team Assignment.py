N = int(input("Enter number of employees: "))
skills = list(map(int, input("Enter skill levels: ").split()))

total_sum = sum(skills)
target = total_sum // 2

dp = [False] * (target + 1)
dp[0] = True

for skill in skills:
    for s in range(target, skill - 1, -1):
        dp[s] = dp[s] or dp[s - skill]

for s in range(target, -1, -1):
    if dp[s]:
        min_diff = total_sum - 2 * s
        break

print(min_diff)
