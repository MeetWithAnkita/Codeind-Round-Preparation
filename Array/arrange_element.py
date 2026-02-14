arr = list(map(int, input("Enter the elements : ").split()))

arr.sort()

print("Increasing order: ",arr)
print("Decreasing order: ",arr[::-1])