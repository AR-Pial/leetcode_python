class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
# Input: p = [1, 2, 3], q = [1, 2, 3]

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.right = TreeNode(1)



solution = Solution()
print(solution.maxDepth(p))

