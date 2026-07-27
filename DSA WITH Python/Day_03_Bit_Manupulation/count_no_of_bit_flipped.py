# count no of bits to be flipped to convert A to B
start = 3
# 10 --> 1010
goal = 4

# 7 ---> 0111

ans = start ^ goal 
binary = bin(ans)[2:]
cnt = 0
for i in range(len(binary)):
    if binary[i] == '1':
        cnt += 1 
print("No of bit have to flip: ",cnt)

