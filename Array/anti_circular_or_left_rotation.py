arr = list(map(int, input("Enter the array elements: ").split()))
position = int(input("Enter the position:"))

for i in range(position):
    temp = arr[0]
    for j in range(0,len(arr)-1):
        arr[j] = arr[j+1]
    arr[len(arr)-1] = temp
    print(arr)    
