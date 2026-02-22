L_range, U_range = map(int, input("Enter the lower and upper range: ").split())
pallindrome = []
for i in range(L_range, U_range+1):
    if str(i) == str(i)[::-1]:
        pallindrome.append(i)
print(f"All pallindrome numbers with in {L_range} and {U_range}: {pallindrome}")