# b = input()

# def ones_compliment(b):
#     result = ""
#     for i in b:
#         if i == '0':
#             result += '1'
#         else:
#             result += '0'
#     return result

# print(ones_compliment(b))

# ///////////////////////// I M P O R T A N T /////////////////////////
# using List 
b = list(input())

for i in range(len(b)):
    if b[i] == '0':
        b[i] = '1'
    else:
        b[i] = '0'

print("".join(b))


# Time and Space Complexity
# Time Complexity: O(n) (visit each bit once)
# Space Complexity: O(n) (create a new string or list)