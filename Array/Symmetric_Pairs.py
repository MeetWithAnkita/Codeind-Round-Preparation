pairs = []
n = int(input("Enter the no of pairs:"))

for i in  range(n):
    a, b = map(int, input("Enter pair: ").split())
    pairs.append((a,b))

seen = {}
print("Symmentic pairs:")

for a,b in pairs:
    if b in seen and seen[b] == a:
        print((a,b))
    else:
        seen[a] = b