arr = list(map(int, input("Enter the array: ").split()))

from collections import Counter 
freq = {} #empty dictionary

for i in arr:
    freq[i] = freq.get(i, 0) + 1

print(freq)