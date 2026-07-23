n = int(input())
arr = list(map(int, input().split()))

def find_smallest_element(arr):
    min_no = float('inf')
    for i in arr:
        if i < min_no:
            min_no = i
    return min_no

print(find_smallest_element(arr))

# Time

# You visit every element once.

# O(N)
# Space

# Only one extra variable.

# O(1)

# ✅ Optimal.