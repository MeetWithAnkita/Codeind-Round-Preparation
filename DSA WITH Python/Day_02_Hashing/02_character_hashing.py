s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]
# contraints:
# "a" <= s[i] <= "z" ==> 97 - 122 

# freq = {}
# count = 0 
# for i in s:
#     if i in freq:
#         freq[i] += 1 
#     else:
#         freq[i] = 1 
# print(freq)
# for i in q:
#     print(i ,": ", freq.get(i, 0))

# # //////////// another way ////////////
# freq = {}

# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1

# for ch in q:
#     print(f"{ch} : {freq.get(ch, 0)}")

# //////////// another way ////////////

hash_list = [0]*27

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97 
    hash_list[index] += 1 
for ch in q :
    aschii_value = ord(ch)
    index = aschii_value - 97
    print(hash_list[index])


# TC : O(N + M)
# SC: O(1)