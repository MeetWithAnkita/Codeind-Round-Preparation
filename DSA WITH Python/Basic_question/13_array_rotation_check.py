n = int(input())
arr = list(map(int, input().split()))

def check_rotated_sorted(arr):
    count = 0 
    for i in range(n):
        if arr[i] > arr[(i+1) % n]:
            count += 1 
    if count <= 1:
            return "Yes"
    else:
            return "No"


print(check_rotated_sorted(arr))