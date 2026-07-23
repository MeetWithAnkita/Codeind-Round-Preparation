n = int(input())
arr = list(map(int, input().split()))

def remove_duplicates(arr):
    j = 0
    for i in range (1, len(arr)):
        if arr[j] != arr[i]:
            j += 1 
            arr[j] = arr[i]
    return arr[:j+1]

print(remove_duplicates(arr))

# 5 5 2 2 1
# 