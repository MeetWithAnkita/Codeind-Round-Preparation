arr = list(map(float, input("Enter the elements in list: ").split()))
positive = []
negative = []
for i in arr:
    if i == 0:
        print(i , " is Zero.")
    elif i < 0 :
        negative.append(i)
    else:
        positive.append(i)

print("Positive numbers: ",positive)
print("Negative numbers: ",negative)