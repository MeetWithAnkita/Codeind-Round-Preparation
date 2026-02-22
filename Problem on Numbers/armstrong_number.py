L_range, U_range = map(int, input("Enter the lower range and upper range: ").split())
arm = []
for i in range (L_range, U_range+1):
    length = len(str(i))
    sum = 0
    for j in i:
        sum = sum + j ** length
    if sum == i:
        arm.append(i)

print("Armstrong numbers: ",arm)