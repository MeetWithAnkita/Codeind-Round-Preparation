A = list(set(map(int, input("Enter elements of list A: ").split())))
B = list(set(map(int, input("Enter elements of list B: ").split())))



# Using set()

# A = set(A) # remove the duplicate elements 
# B = set(B)

# if B.issubset(A) == True:
#     print("Set B is a subset of set A")
# else:
#     print("Set B is not a subset of Set A") 

# without using set 
is_subset = True
for i in B :
    if i not in A:
        is_subset = False
        break
    
if is_subset == True : 
    print("B is a subset of A.")
else:
    print("B is not a subset of A")