# n = int(input())
# k = int(input())
# arr = list(map(int, input().split()))

# def rotate_array(arr):
#     # p = arr[(n - k ):]
#     # q = arr[:(n-k)]
#     return (arr[n-k:] + arr[:n-k])

# # print(rotate_array(arr))
# Time Complexity: O(N)
# Space Complexity: O(N) 


# ////////////////////////////////////////////////////////////////////////////////


# Reversal Algorithm
# Demonstrates knowledge of two pointers and in-place array manipulation.

k = int(input())
arr = list(map(int, input().split()))
def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate_array(arr, k):
    n = len(arr)
    k %= n

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

    return arr

print(rotate_array(arr, k))

# Time Complexity: O(N)
# Space Complexity: O(1) ✅
