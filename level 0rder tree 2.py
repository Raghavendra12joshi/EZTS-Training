class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

def levelorder(root):
    if not root:
        return
    
    Q = [root]  # Initialize the queue with the root node
    Q.append(None)  # Marker for end of the current level

    while len(Q) > 0:
        curr = Q.pop(0)
        
        if curr is None:
            if len(Q) == 0:
                break
            else:
                print()  # Print a newline to separate levels
                Q.append(None)  # Add marker for the next level
        else:
            print(curr.value, end=" ")
            if curr.left is not None:
                Q.append(curr.left)
            if curr.right is not None:
                Q.append(curr.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right.right.right = Node(11)
    root.left.right.left.left = Node(12)
    root.left.right.left.right = Node(13)

    levelorder(root)
