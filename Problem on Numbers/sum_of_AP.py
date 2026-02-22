# 2 5 8 11 14
# a = First term = 2
# d = Common Difference = 3
# n = number of terms = 5



# method 1 ----------------
# sum(n) = (n/2) * [2a + (n - 1)*d]

# a = float(input("Enter the first term: "))
# d = float(input("Enter the difference: "))
# n = int(input("Enter the number of terms: "))

# sum = (n/2) * ((2*a) + (n - 1) * d)
# print("Sum: ", sum)



# method 2 -------------

# a = float(input("Enter the first term: "))
# d = float(input("Enter the difference: "))
# n = int(input("Enter the number of terms: "))
# total = 0 
# for i in range(n):
#     total +=  a
#     a += d

# print("Sum: ", total)



# Method 3-----------
# sum(n) = (n/2) * (a + l)

a = float(input("Enter the first element: "))
l = float(input("Enter the last element: "))
n = int(input("Enter the number of terms: "))

sum_ap = (n/2) * (a + l)
print("SUM of AP: ", sum_ap)
