n = int(input())
arr = list(map(int, input().split()))
def find_large_element(arr):
    largest = arr[0]
    for num in arr :
        if num > largest:
            largest = num
    print(largest) 

find_large_element(arr)

# Time Complexity: O(N)
# Space Complexity: O(1)