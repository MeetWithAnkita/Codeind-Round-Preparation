n = int(input())

ans = n & (n-1)
if ans == 0 and n>0:
    print("n is power of 2")
else:
    print("n is not power of 2")


# Time Complexity
# Time: O(1)
# Space: O(1)