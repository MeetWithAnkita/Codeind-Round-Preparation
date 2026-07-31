n = int(input())
arr = list(map(int, input().split()))

def find_2_major_element(arr):
    candidate1 = None 
    candidate2 = None
    count1 = 0 
    count2 = 0 

    for i in arr:        
        if candidate1 == i:
            count1 += 1 
        elif candidate2 == i :
            count2 += 1
        elif count1 == 0 :
            candidate1 = i 
            count1 = 1 
        elif count2 == 0:
            candidate2 = i
            count2 = 1
        else:
            count1 -= 1 
            count2 -= 1

    # ---------- Second Pass (Verify Candidates) ----------
    count1 = 0
    count2 = 0

    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    ans = []

    if count1 > len(arr) // 3:
        ans.append(candidate1)

    if count2 > len(arr) // 3:
        ans.append(candidate2)

    return ans

print(find_2_major_element(arr))


# Complexity
# Time Complexity: O(n)
# First pass: O(n)
# Second pass: O(n)
# Total: O(2n) = O(n)
# Space Complexity: O(1)
# Only four variables 
# (candidate1, candidate2, count1, count2) and 
# a small result list are used.