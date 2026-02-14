arr = list(map(int, input("Enter the elements in array:").split()))
large = arr[0]
for i in range (len(arr)):
    if large < arr[i]:
        large = arr[i]
print("Largest element is:", large)