# arr = [1,2,3,4,5]
# 1st ==> [5,1,2,3,4]
# 2nd ==> [4,5,1,2,3]
arr = list(map(int, input("Enter the numbers of array:").split()))
position = int(input("Enter the position change: "))


# for i in range(position):
#     arr = arr[-1:] + arr[:-1]
#     print(arr)

for i in range(position):
    temp = arr[len(arr) -1]
    for j in range(len(arr)-1, 0, -1):
        arr[j] = arr[j-1]
    arr[0] = temp
    print(arr)


# print(arr)