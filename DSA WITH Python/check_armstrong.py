n = 1634
l = len(str(n))
num = n
result = 0
while n>0:
    l_d = n % 10 
    result = result + pow(l_d, l)
    n = n // 10 
if num == result :
    print("Yes")
else:
    print("No")    