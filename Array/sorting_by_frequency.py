# arr = [2,3,3,4,2,4,4,3,4]
# a = 2, 3 = 3, 4 = 4
# output: [4,4,4,4,3,3,3,2,2]
from collections import Counter 
arr = list(map(int, input("Enter the array elements:").split()))
# freq={} 
# for num in arr:
#     freq[num] = freq.get(num, 0) + 1
# print(freq)

freq = Counter(arr)
print(freq)

arr.sort(key = lambda x: (-freq[x], x))
print("Sorted by frequency: ", arr)