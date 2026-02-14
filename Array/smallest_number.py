arr= list(map(int, input("Enter the elements in array: ").split()))

small = arr[0]
for i in range(len(arr)):
    if small > arr[i]:
        small = arr[i]
print("Smallest number in array is:", small)