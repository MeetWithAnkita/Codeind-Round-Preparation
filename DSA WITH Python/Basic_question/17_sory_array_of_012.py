# Dutch National Flag Algorithm 

n = int(input()) 
arr = list(map(int, input().split()))

def dutch_national(arr):
    low = 0
    mid = 0
    high = n-1
    while mid <= high:
        if arr[mid] == 0 :
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1 
            mid += 1 
        elif arr[mid] == 1 :
            mid += 1 
        else :
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print(dutch_national(arr))