n = int(input())
arr = list(map(int, input().split()))

def moveZeroes(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] ,arr[j] = arr[j] ,arr[i]
            j+=1
    return arr

print(moveZeroes(arr))
# 0 5 0 2 1 
# 5 0 0 2 1 
# 5 2 0 0 1
# 5 2 1 0 0 

# Time Complexity: O(N) ✅
# Space Complexity: O(1) ✅