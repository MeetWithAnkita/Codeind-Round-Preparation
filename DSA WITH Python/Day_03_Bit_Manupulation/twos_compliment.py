b = input()
def twos_climent(b):
    result = ""
    for i in b:
        if i == '0':
            result += '1'
        else:
            result += '0'
    # 2's Compliment....................///////////            
    ans = (int(result,2) + 1)
    return bin(ans)[2:].zfill(len(b))

print(twos_climent(b))