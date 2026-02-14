arr = list(map(int, input("Enter the elements of the array: ").split()))
n = len(arr)

arr.sort() #Here array must be sorted 
print("Sorted aray: ", arr)

if n % 2 ==  1: #odd
    median = arr[n // 2]
else: #even 
    median = (arr[n//2 -1] + arr[n//2]) // 2

print("The median is: ", median)