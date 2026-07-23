n = int(input())
arr = list(map(int, input().split()))

def check_sorted(arr):
    for i in range(len(arr) - 1 ):
        if arr[i] > arr[i+1]:
            return "Not SOrted"
    return "Sorted"

print(check_sorted(arr))
        

# Time Complexity: ✅ O(N)
# Traverse the array once.

# Space Complexity: ✅ O(1)
# No extra array is used.
