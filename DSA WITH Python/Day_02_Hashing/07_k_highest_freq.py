# # # ////////// 1st Way //////////
# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input()) 

# def top_k_freq(arr, k):
#     freq = {}
#     for i in arr:
#         freq[i] = freq.get(i, 0) + 1 

#     #sorted base on freq
#     sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse = True )

#     # take first K elements 
#     ans = []
#     for i in range (k):
#         ans.append(sorted_freq[i][0])
#     return ans
# print(top_k_freq(arr, k))

# # Time:  O(n log n)
# # Space: O(n)


# # ////////// 2nd Way [ Min Heap of size K ]//////////
# import heapq

# n = int(input())
# arr = list(map(int,input().split()))
# k = int(input())

# def top_k_frequent(arr,k):
#     freq = {}
#     for num in arr:
#         freq[num] = freq.get(num,0)+1

#     # Step 2: Min Heap
#     heap = []

#     for num,count in freq.items():
#         heapq.heappush(heap,(count,num))
#         if len(heap) > k:
#             heapq.heappop(heap)


#     # Step 3: Extract answer
#     ans = []

#     while heap:
#         count,num = heapq.heappop(heap)
#         ans.append(num)

#     return ans


# print(top_k_frequent(arr,k))
# # TC: O(n log k)
# # SC: O(n)



# /////////// BUcket Sort //////////
n = int(input())
arr = list(map(int, input().split()))
k = int(input())


def top_k_frequent(arr, k):

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: Create buckets
    # index represents frequency
    bucket = [[] for _ in range(len(arr) + 1)]


    # Step 3: Put numbers into buckets
    for num, count in freq.items():
        bucket[count].append(num)


    # Step 4: Collect top K elements
    ans = []

    for frequency in range(len(bucket)-1, 0, -1):

        for num in bucket[frequency]:
            ans.append(num)

            if len(ans) == k:
                return ans
    return ans


print(top_k_frequent(arr, k))