n = int(input())
arr = list(map(int, input().split()))
def major_element(arr):
    freq ={}
    for num in  arr:
        freq[num] = freq.get(num, 0) + 1 

    for k in freq:
        if freq[k] > len(arr)// 2:
            return k
    return -1 

print(major_element(arr))

# TC: O(N)
# SC: O(N)   --> O(1) using Optimal (Boyer-Moore Voting)

# ////////// Optimal (Boyer-Moore Voting) //////////

# def majority(arr):
#     candidate = None 
#     count = 0 

#     for i in arr :
#         if count == 0:
#             candidate = i
#         if i == candidate:
#             count += 1 
#         else:
#             count -= 1
#     return candidate 
# print(majority(arr))

# TC: O(N)
# SC: O(1)


