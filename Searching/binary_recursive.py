arr = list(map(int, input("Enter the numbers of array using space separator: ").split()))
arr.sort()
print("Sorted array is: ", arr)
key = int(input("Enter the searching element: "))
L = 0
U = len(arr) - 1

def binary_searching(arr, key, L, U):
    if L > U:
        print("Element not found.")
        return 
    mid = (L + U)//2
    if key == arr[mid]:
        print(f"{key} found at {mid} index.")
    elif key > arr[mid]:
        binary_searching(arr, key, mid+1, U)
    else: 
        binary_searching(arr, key, L, mid-1)
    

binary_searching(arr, key, L, U)