# Given an array and a target, find indices of the two numbers that add up to the target. Each input has exactly one solution.

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

# def reach_target(arr, target):
#     freq ={}

#     for i in range (len(arr)):
#         req = target - arr[i]
#         if req in freq:
#             return freq[req], i
#         freq[arr[i]] = i

# print(reach_target(arr, target))


# def all_two_sum(arr, target):
#     freq = {}
#     ans = []

#     for i in range (len(arr)):
#         req = target - arr[i]
#         if req in freq :
#             ans.append((freq[req], i))
#         freq[arr[i]] = i 
#     return ans 
# print(all_two_sum(arr, target))

# TC: O(N)


from collections import defaultdict

def all_pairs(arr, target):
    freq = defaultdict(list)
    ans = []

    for i, num in enumerate(arr):
        required = target - num

        for j in freq[required]:
            ans.append((j, i))

        freq[num].append(i)

    return ans

# arr = [3, 3, 3]
# target = 6

print(all_pairs(arr, target))





