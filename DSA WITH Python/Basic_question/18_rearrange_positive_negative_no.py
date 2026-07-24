n = int(input())
arr = list(map(int, input().split()))
# Rearrange the array such that positive and negative numbers alternate,
# starting with a positive number. Maintain relative order

def arrange(arr):
    p = []
    n = []
    for i in arr:
        if i > 0:
            p.append(i)
        else:
            n.append(i)
    answer = []
    for i in range (len(p)):
        answer.append(p[i])
        answer.append(n[i])

        return answer

print(arrange(arr))    