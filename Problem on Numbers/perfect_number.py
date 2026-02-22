lower_range, upper_range = map(int,input("Enter the lower range and upper range: ").split())
no = []
for i in range(lower_range, upper_range+1):
    # no = []
    sum = 0
    for j in range (1, i//2+1):
        if i % j == 0:
            sum += j
    if i == sum:
        no.append(i)

print("Perfect numbers: ", no)
