# Method 1 : Recursive 

class Node:
    def __init__(self, data):
        self.data = data # 1 
        self.left = None
        self.right = None 

from collections import deque 

# Function to build a tree from user input( level order )
def build_tree():
    data = list(map(int, input("Enter nodes in level order (-1 for None): ").split()))
    # data = [1 2 3 4 5 -1 6]
    if not data : 
        return None 
    
    if data[0] == -1:
        return None
    
    root = Node(data[0]) #root = 1
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        current = queue.popleft()

        if i < len(data) and data[i] != -1:
            current.left = Node(data[i])
            queue.append(current.left)
        i += 1 

        if i < len(data) and data[i] != -1:
            current.right = Node(data[i])
            queue.append(current.right)
        i += 1
    return root 

def height(node):
    if node is None:
        return 0 
    
    left_height = height (node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)

root = build_tree()
h = height(root)
print("Height of the tree: ",h)

# Method 2 : Iterative 