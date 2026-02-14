arr = list(map(int, input("Enter the elements in array:").split()))

# A = set(arr)
# repeat = []
# count = 1
# for i in range(0,len(arr)-1):
#     if arr[i] == arr[i+ 1]:
#         count +=1 
#     if count > 1:
#         if arr[i] not in repeat:
#             repeat.append(arr[i])
# print(repeat)

repeat = [x for x in set(arr) if arr.count(x) > 1]

print(repeat)