n = [5,3,2,2,1,5,5,7,5,10]
m = [10,11,1,9,5,67,2]
# constrains:
# i> 1<= n[i] <= 10
# ii> n can have 10^8 elements
# iii> m can have 10^8 elements
# ////////////////////////////////////////////////////////////

# for i in m:
#     count = 0 
#     for j in n:
#         if i == j:
#             count += 1 
#     print(i ," = ", count)
# # TC: O(N*M)
# # SC: O(1)

# //////////// optimal Solution //////////// 
# if i> constrains have ==> Then it will applicable 
# otherwise dict + hashing is GOOD CHOICE.

# hash_list = [0] * 11 
# for i in n:
#     hash_list[i] += 1 
# for num in m:
#     if num < 0 or num > 10:
#         print(num, ": 0")
#     else:
#         print(num, " : ",hash_list[num])

# TC: O(N + M)
# SC: O(1)


# //////////// DICTIONARY + HASHING ////////////
freq = {} # frequcecy dict

for num in n:
    if num in freq:
        freq[num] += 1 
    else:
        freq[num] = 1
for num in m:
    print(num, ": ", freq.get(num, 0))

# TC: O(N + M)
# SC: O(K) || k = no of unique values 




