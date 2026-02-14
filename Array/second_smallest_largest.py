arr = list(map(int, input("Enter the elemenrs in list:").split()))
arr = list(set(arr)) #remove any duplicate element if presents 

if len(arr) <2 :
    print("Not enough element")
else: 
    arr.sort()
    print("Second smallest:", arr[1])
    print("Second largest:", arr[-2])