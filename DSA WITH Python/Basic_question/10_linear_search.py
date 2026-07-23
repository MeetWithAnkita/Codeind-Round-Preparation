n = int(input())
arr = list(map(int, input().split()))
target = int(input())

def linear_searcch(arr, target):
    for i in arr:
        if target == i:
            return "Found"
            
    return "Not Found"

print(linear_searcch(arr, target))

# TC: O(n)
# SC: O(1)