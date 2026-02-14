arr = list(map(int, input("Enter the numbers in list:").split()))
arr.sort()
print(f"The sorted array is: {arr}")
key = int(input("Enter the searching element: "))

L = 0
U = len(arr) - 1 

while L <= U:
    mid = (L + U) // 2

    if arr[mid] == key:
        print(f"{key} is found at {mid} index.")
        break
    elif key > arr[mid]:
        L = mid + 1
    else: 
        L = mid - 1 


    