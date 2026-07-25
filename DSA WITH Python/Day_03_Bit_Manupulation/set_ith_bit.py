n = int(input())
i = int(input())

def set_1(n, i):
    # binary = int(bin(n)[2:])
    x = 1 << i
    ans = n | x 
    return ans 

print(set_1(n, i))

# TC: O(1)