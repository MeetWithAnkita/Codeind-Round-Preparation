arr = list(map(int, input("Enter the elements: ").split()))
length = len(arr)

for i in range(1, length-1):
    right = 0
    left = 0 
    for j in range(0,i):
        left += arr[j]
    for k in range(i+1, length):
        right += arr[k]
    
    if left == right:
        print("This Array is Equilibrium.")
        break
    else:
        continue
else:
    print("It is not an equilibrium array.")
