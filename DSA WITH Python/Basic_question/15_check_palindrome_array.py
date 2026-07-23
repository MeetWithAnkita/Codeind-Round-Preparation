# n = int(input())
# arr = list(map(int, input().split()))

# def check_palindrome_list(arr):
#     for i in range(int(n/2)):
#         if arr[i] != arr[n-i-1]:
#             return 'Not Palindrome'
                    
#     return 'Palindrome'


# print(check_palindrome_list(arr))

# 0 1 2 3 4 
# i = 0 , j = 5 - i - 1 = 4
# i = 1 , j = 5 - i - 1 


# using two pointer
n = int(input())
arr = list(map(int, input().split()))

def check_palindrome_list(arr):
    left = 0 
    right = n-1
    while left < right :
        if arr[left] != arr[right]:
            return 'Not Palindrome'
        left += 1 
        right -= 1
    return 'Palindrome'


print(check_palindrome_list(arr))