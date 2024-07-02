class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_leaf_nodes(root):
    if not root:
        return

    if not root.left and not root.right:
        print(root.val, end=" ") 

    print_leaf_nodes(root.left)  
    print_leaf_nodes(root.right) 

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print("Leaf nodes of the BST:")
print_leaf_nodes(root)