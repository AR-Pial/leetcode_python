class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    def ino_traverse(node):
        if not node:
            return
        ino_traverse(node.left)
        result.append(node.val)
        ino_traverse(node.right)
    ino_traverse(root)
    return result

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(inorderTraversal(root1))