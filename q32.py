class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_leaf_nodes(node):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        print(node.value, end=" ")
    
    print_leaf_nodes(node.left)
    print_leaf_nodes(node.right)

# Example usage
root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
print("Leaf nodes of the BST:")
print_leaf_nodes(root)
