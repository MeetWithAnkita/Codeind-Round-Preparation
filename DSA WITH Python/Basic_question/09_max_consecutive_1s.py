n = int(input())
b_arr = list(map(int, input().split()))

def max_consecutive_one(b_arr):
    max_count = 0
    current = 0
    for i in b_arr:
        if i == 1:
            current += 1
            if current > max_count:
                max_count = current 
        else:
            current = 0
    return max_count
print(max_consecutive_one(b_arr))

# Complexity
# Time

# You visit each element once.

# O(N)
# Space

# Only two variables are used.

# O(1)

# ✅ Optimal