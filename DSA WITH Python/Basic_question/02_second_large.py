n = int(input())
arr = list(map(int,input().split()))

def second_large(arr):
    large = float('-inf')
    s_large = float('-inf')

    for num in arr:
        if num > large :
            s_large = large
            large = num 
        elif large > num > s_large :
            s_large = num 

    if s_large == float('-inf'):
        return - 1 
    
    return s_large 


print(second_large(arr)    )


# Complexity
# Time Complexity: O(N) ✅
# Space Complexity: O(1) ✅

# This is the optimal solution.