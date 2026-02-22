num = int(input("Enter a number or alphabet series: "))

# For both type of input:::::::::------------------------
# if num == num[::-1]:
#     print("It is a pallindrome no")
# else:
#     print("It is not an pallindrome no")

# Manual and for number:::::::::::::-------------------------
no = num
rev = 0
while num > 0:
    digit = num % 10 
    rev = rev * 10 + digit 
    num = num //10

if rev == no:
    print("Yes, It is a pallindrome no.")
else:
    print("It is not an pallindrome no.")
