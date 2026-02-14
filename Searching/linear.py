arr = list(map(int, input("Enter the elements:").split()))
key = int(input("Enter the searching element:"))

found = False
for i in range (len(arr)):
    if arr[i] == key:
        print(f"{key} is found at {i} index.")
        found = True
        break
if not found:
        print("Element not found")