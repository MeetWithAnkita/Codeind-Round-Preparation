A = input("Enter the elements of A :").split()
B =input("Enter the elements of B: ").split()

# arrange the element of A as per element of B 
element=[]
for i in B:
    while i in A:
        element.append(i)
        A.remove(i)

print(element)