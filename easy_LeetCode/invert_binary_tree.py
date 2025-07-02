
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the tree
sol = Solution()
res = sol.invertTree(root)
sol = Solution()
res = sol.invertTree(root)
def print_tree(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.val, end=' ')
            queue.append(node.left)
            queue.append(node.right)

print_tree(res)