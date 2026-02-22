L_range, U_range = map(int, input("Enter the lower range and upper range: ").split())
prime = []
for i in range(L_range, U_range+1):
    if i > 1:
        for j in range(2, i//2):
            if i % j == 0:
                break
        else:
                prime.append(i)
            
print("Prime numbers: ",prime)

