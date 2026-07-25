n = int(input())
i = int(input())

x = 1<<i
res = n & (~x)

print(res)

# TC : O(1)
# SC : O(1)