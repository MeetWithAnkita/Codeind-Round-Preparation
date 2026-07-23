n = int(input())
arr = list(map(int, input().split()))

def count_even_odd(arr):
    odd = 0 
    even = 0
    for i in arr:
        if i % 2 == 0 :
            even += 1
        else:
            odd += 1 

    print("Even=",even,"  Odd=",odd)

count_even_odd(arr)

# Complexity
# Time Complexity

# You traverse the array once.

# O(N)
# Space Complexity

# Only two variables.

# O(1)

# ✅ Optimal