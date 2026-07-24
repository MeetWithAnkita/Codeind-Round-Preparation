# b = int(input())

# def binary_to_decimal(b):
#     # 1101
#     ans = 0 
#     for i in range (len(str(b))):
#         l = b % 10 
#         ans += l * pow(2,i)
#         b = b // 10 
#     return ans

# print(binary_to_decimal(b))

# TC = O(n)
# SC = O(1)




b = input()

def binary_to_decimal(b):
    d_no = 0 
    power = 0 
    index = len(b)-1 #5
    while index >= 0 :
        num = int(b[index]) * (2 ** power)
        d_no += num
        index -= 1 
        power += 1 
    return d_no

print(binary_to_decimal(b))