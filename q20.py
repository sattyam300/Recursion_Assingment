class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, X):
    if not root:
        return TreeNode(X)  

    if X < root.val:
        root.left = insert(root.left, X) 
    else:
        root.right = insert(root.right, X)

    return root

root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)