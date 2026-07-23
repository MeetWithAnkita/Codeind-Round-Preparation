# n = int(input())
# arr = list(map(int, input().split()))

# def find_missing_no(arr):
#     expected = (n * (n+1)) /2
#     actual = 0
#     for i in arr:
#         actual += i 

#     return int(expected - actual)

# print( find_missing_no(arr))

# TC = O(n)
# SC = O(1)


# ///////////////////////////////////////////////
# # Using XOR 
# n = int(input())
# arr = list(map(int, input().split()))

# def find_missing_no(arr):
#     xor = 0 
#     for i in range(n + 1):
#         xor ^= i
#     for num in arr:
#         xor ^= num
#     return xor


# print( find_missing_no(arr))

# /////////////////////////////////////////
n = int(input())
arr = list(map(int, input().split()))

def find_missing_no(arr):
    xor = n 
    for i in range (n):
        xor ^= i
        xor ^= arr[i]

    return xor

print( find_missing_no(arr))



# Complexity

# Both methods are:

# Time: O(N)
# Space: O(1)