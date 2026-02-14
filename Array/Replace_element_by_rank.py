arr = list(map(int, input("Enter the elements: ").split()))



unique_sorted = sorted(set(arr))

rank = {} # empty dictonary 
for i, val in enumerate(unique_sorted):
    rank[val] = i+1

print(rank)
result = [rank[x] for x in arr]

print("Array with ranks:", result)