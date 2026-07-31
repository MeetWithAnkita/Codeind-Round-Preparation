# ////////// Only for k = 2 //////////
# n = int(input("Length of array: "))
# arr = list(map(int, input("Array: ").split()))
# k = int(input("No of sub-array: "))

# def max_dominance_score(arr):
#     max_d_s = 0

#     for i in range(1, n):

#         freq = {}
#         for j in range(i):
#             freq[arr[j]] = freq.get(arr[j], 0) + 1
#         left = max(freq.values())

#         freq1 = {}
#         for j in range(i, n):
#             freq1[arr[j]] = freq1.get(arr[j], 0) + 1
#         right = max(freq1.values())

#         max_d_s = max(max_d_s, left + right)

#     return max_d_s

# if k != 2:
#     print("This solution works only for K = 2.")
# else:
#     print(max_dominance_score(arr))



# ////////// Using Dynamic Programming //////////
n, K = map(int, input().split())
arr = list(map(int, input().split()))

INF = float('-inf')

dp = [[INF] * (K + 1) for _ in range(n + 1)]
dp[0][0] = 0

for p in range(1, K + 1):
    for i in range(1, n + 1):

        freq = {}
        best = 0

        # Build the last subarray backwards
        for j in range(i, 0, -1):

            x = arr[j - 1]
            freq[x] = freq.get(x, 0) + 1
            best = max(best, freq[x])

            if dp[j - 1][p - 1] != INF:
                dp[i][p] = max(dp[i][p],
                               dp[j - 1][p - 1] + best)

print(dp[n][K])

# Time: O(K × N²)
# Space: O(K × N)