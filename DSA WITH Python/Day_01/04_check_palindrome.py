# n = 12321

# def check(n):
#     num = n
#     if str(num) == str(n)[::-1]:
#         print("Yes")
# check(n)



n = 1234321
num = n 
d = 0 
while n>0:
    l_d = n% 10 
    d = d * 10 + l_d
    n = n//10
if d == num:
    print("Yes")
else:
    print("No")