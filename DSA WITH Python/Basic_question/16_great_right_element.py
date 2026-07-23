n = int(input())
arr = list(map(int, input().split()))

def replace_with_great_right_element(arr):
    max_value = -1
    for i in range (n-1, 0, -1):
        a = arr[i]
        arr[i] = max_value
        if max_value < a:
            max_value = a
    return arr

print(replace_with_great_right_element(arr))