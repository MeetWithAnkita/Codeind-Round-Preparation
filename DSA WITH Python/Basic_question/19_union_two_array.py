# n1 = int(input("1st Array size: "))
# a1 = list(map(int, input().split()))
# n2 = int(input("2nd Array size: "))
# a2 = list(map(int, input().split()))

# def remove_duplicates(arr):
#     j = 0 
#     for i in range (1, len(arr)):
#         if arr[j] != arr[i]:
#             j += 1 
#             arr[j] = arr[i]
#     return arr[:j+1]

# def union_array(a1, a2):
#     new_array = sorted(a1 + a2)
#     new_array = remove_duplicates(new_array)
#     return new_array

# print(union_array(a1, a2))

# # ///////////////////////// I M P O R T A N T /////////////////////////
# #  work on two sorted array 
# a1 = list(map(int, input("First Array: ").split()))
# a2 = list(map(int, input("Second Array: ").split()))

# def find_union(a1, a2):
#     i = 0
#     j = 0 
#     answer = []
#     while i<len(a1) and j<len(a2):
#         if a1[i] < a2[j]:
#             if not answer or answer[-1] != a1[i]:
#                 answer.append(a1[i])
#             i+= 1 
#         elif a1[i] > a2[j]:
#                 if not answer or answer[-1] != a2[j]:
#                     answer.append(a2[j])
#                 j+= 1 
#         else: # a1[i] == a2[j]
#             if not answer or answer[-1] != a1[i]:
#                   answer.append(a1[i])
#             i += 1 
#             j += 1
#     while i < len(a1):
#         if not answer or answer[-1] != a1[i]:
#             answer.append(a1[i])
#         i+= 1 
#     while j < len(a2):
#         if not answer or answer[-1] != a2[j]:
#             answer.append(a2[j])
#         j+= 1
#     print(answer)

# find_union(a1, a2)
         


# Your approach (sort + remove duplicates):
# Time: O((n + m) log(n + m))
# Space: O(n + m)
# Two-pointer approach (expected in interviews for sorted arrays):
# Time: O(n + m) ✅
# Space: O(n + m)


# ///////////////////
# # set use
# a1 = [1,2,2,3]
# a2 = [2,3,4]

# union = set(a1 + a2)

# print(union)


# ///////////////////////// I M P O R T A N T /////////////////////////
#  Unsorted Array 

a1 = list(map(int, input("First Array: ").split()))
a2 = list(map(int, input("Second Array: ").split()))
def find_union(a1, a2):
    answer = set()
    for num in a1:
        answer.add(num)
    for num in a2:
        answer.add(num)
    return list(answer)

print(find_union(a1, a2))


