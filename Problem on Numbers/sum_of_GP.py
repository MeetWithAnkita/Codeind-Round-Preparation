# 2 6 18 54 162
# a = first term 
# r = common ratio = 3
# sum_GP = a * ((r^n -1) / (r - 1))
# 
a = float(input("Enter the first element: "))
r = float(input("Enter the comon ratio: "))
n = int(input("Enter the terms: "))

if r == 1:
    sum_gp = a * n 
else:
    sum_gp = a * (r**n - 1) / (r -1 )

print(sum_gp)