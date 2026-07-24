# # ///////////////////////// I M P O R T A N T /////////////////////////
# Unsorted Array 
# a1 = list(map(int, input("First Array: ").split()))
# a2 = list(map(int, input("Second Array: ").split()))

# def find_intersection(a1, a2):
#     answer = []
    
#     for i in range (len(a1)):
#            for j in range (len(a2)): #Time Complexity = O(N × M)
#                 if a1[i] == a2[j]:
#                     answer.append(a1[i])
#                     continue
#     return set(answer)

# print(find_intersection(a1, a2))

# ///////////////////////// I M P O R T A N T /////////////////////////
# unsorted Array 
# a1 = list(map(int, input("First Array: ").split()))
# a2 = list(map(int, input("Second Array: ").split()))

# def find_intersection(a1, a2):
#     answer = set()
#     for num in set(a1):
#         if num in set(a2):
#             answer.add(num)
#     return list(answer)
# print(find_intersection(a1, a2))
# # TC: O(N + M) average
# # SC: O(M)


# ///////////////////////// I M P O R T A N T /////////////////////////
# sorted array 
# two pointer 
a1 = list(map(int, input("First Array: ").split()))
a2 = list(map(int, input("Second Array: ").split()))

def find_intersection(a1, a2):
    i = 0 
    j = 0 
    answer = []
    while i<len(a1) and j <len(a2):
        if a1[i] < a2[j]:
            i+= 1 
        elif a1[i] > a2[j]:
            j+= 1 
        else :
            if not answer or answer[-1] != a1[i]:
                answer.append(a1[i])
            i += 1 
            j += 1 
    return answer 
print(find_intersection(a1, a2))

# # TC: O(N + M) average
# # SC: O(M)