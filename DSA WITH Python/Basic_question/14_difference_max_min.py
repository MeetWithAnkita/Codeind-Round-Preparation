n = int(input())
arr = list(map(int, input().split()))

def diff_min_max(arr):
    maximum = float('-inf')
    minimum = float('inf')
    for i in arr:
        if i < minimum :
            minimum = i 
        if i > maximum:
            maximum = i 
    return (maximum - minimum)

print(diff_min_max(arr))


# Complexity
# Time Complexity: O(N) ✅
# Space Complexity: O(1) ✅