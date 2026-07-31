n = int(input())
arr = list(map(int, input().split()))

def check_duplicate(arr):
    freq = {}
    for i in range(len(arr)):
        if arr[i] not in freq:
            freq[arr[i]] = i
        else:
            return True
    return False
print(check_duplicate(arr))

# Time Complexity: ✅ O(n)
# Space Complexity: ✅ O(n)
