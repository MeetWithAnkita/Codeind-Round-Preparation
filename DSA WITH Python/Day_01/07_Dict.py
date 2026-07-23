# Distionary / Frequency Map 
# nums = [5,6,7,7,1,9,111,1,1,5,1,1]

# frequency_map = dict()
# for i in range (0, len(nums)):
#     if nums[i] in frequency_map:
#         frequency_map[nums[i]] += 1 
#     else:
#         frequency_map[nums[i]] = 1
# print(frequency_map)


# Using hash-map 
nums = [5,6,7,7,1,9,111,1,1,5,1,1]
hash_map = dict()
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0) + 1

print(hash_map)
