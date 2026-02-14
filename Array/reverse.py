arr = list(map(int, input("Enter the elements for array: ").split()))

# Slicing
# print("Reverse the array: ",arr[::-1] )

# reverse()
# arr.reverse()
# print("Reverse the array: ",arr)

# using Loop
rev=[]
for i in range(len(arr)-1, -1, -1): #range(start, stop, jump)
    rev.append(arr[i])
print("Reserved array:", rev)

# Swap element
# L = 0 
# U = len(arr) -1

# while L < U:
#     arr[L], arr[U] = arr[U], arr[L]
#     L += 1
#     U -= 1
# print("Reversed array:", arr)