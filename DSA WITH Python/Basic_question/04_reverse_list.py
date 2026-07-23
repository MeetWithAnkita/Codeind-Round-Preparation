n = int(input())
arr = list(map(int, input().split()))

# def reverse_list(arr):
#     for i in range(n-1, -1, -1):
#         print(arr[i], end= ' ')
# reverse_list(arr)
def reverse_list(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverse_list(arr))

# Time Complexity: O(N)
# Space Complexity: O(1)
