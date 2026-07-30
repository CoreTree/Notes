class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def print_level_order(root):
    if root is None:
        return
    
    queue = [ root ]

    while len(queue) > 0:
        print(queue[0].data, end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    print_level_order(root)

#
# Tree design:
#                1
#       2                  3
#   4       5           6      7
# 8  9   10  11      12 13   14 15
#