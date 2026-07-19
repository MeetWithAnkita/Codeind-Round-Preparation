count = 0 
n = 511156
num = n
while num > 0 :
    l_d = num % 10 
    count= count + 1 
    num = num // 10 
print("Length = ",count)    

from math import * 
n = 511156
num = n
def count_digit(num):
    return int(log10(num) + 1)
print(count_digit(num))