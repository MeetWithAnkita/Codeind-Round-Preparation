arr = list(map(int, input("Enter the array: ").split()))
n = len(arr)                                  #n = 5 

for i in range(n):                            #0
    for j in range(0,n-i-1 ):                 #5-0-1= 4
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Increaseing order: ", arr)

arr.reverse()
print("Decreasing: ",arr)