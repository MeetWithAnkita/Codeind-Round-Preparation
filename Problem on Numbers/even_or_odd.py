lower, upper = map(int, input("Enter the lower and upper range: ").split())

odd = []
even = []
for i in range(lower, upper+1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even No: ",even)
print("Odd nos: ",odd)