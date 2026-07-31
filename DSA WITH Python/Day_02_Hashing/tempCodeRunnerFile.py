def major_element(arr):
    freq ={}
    for num in  arr:
        freq[num] = freq.get(num, 0) + 1 

    for k in freq:
        if freq[k] > len(arr)// 2:
            return k
    return -1 

print(major_element(arr))