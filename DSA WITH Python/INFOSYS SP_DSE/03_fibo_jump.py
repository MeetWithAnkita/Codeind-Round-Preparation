N, A, B = map(int, input().split())

fib = [1, 2, 3, 5, 8]
INF = float('inf')

dp = [INF] * (N+1)
dp[1] = 0 

for i in range(1, N+1):
    if dp[i] == INF:
        continue
    for jump in fib:
        nxt = i + jump
        if nxt <= N:
            cost = A + (B * jump)
            dp[nxt] = min(dp[nxt] , dp[i] + cost)
print(dp[N])

# Time Complexity: O(5 × N) = O(N)
# Space Complexity: O(N)

# This is the optimal dynamic programming solution.


# 10 5 2
# 28