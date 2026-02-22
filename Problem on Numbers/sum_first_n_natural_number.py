# sum(n) = n * (n+1) // 2

n = int(input("Enter the n-th natural numbers: "))

# sum = ( n * (n+1) ) // 2
# print(f"Sum of {n}th sumbers: {sum}")

sum = 0
for i in range(1, n+1):
    sum += i
print(f"Sum of {n}th sumbers: {sum}")