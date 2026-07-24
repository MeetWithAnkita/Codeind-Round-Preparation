d = int(input())

def convert_to_binary(d):
    result = []
    while d > 0:
        b = d % 2 
        result.append(str(b))
        d //= 2 
    return ''.join(result[::-1])

print(convert_to_binary(d))

# TC: O(log n)
# SC: O(log n)

# ///////////////////////// I M P O R T A N T /////////////////////////

